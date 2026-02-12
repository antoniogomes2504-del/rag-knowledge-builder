import re
from docx import Document
from pypdf import PdfReader
import tiktoken
import os

def count_tokens(text, encoder):
    return len(encoder.encode(text))

def extract_text(path):
    if path.endswith(".docx"):
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

    elif path.endswith(".pdf"):
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            extract = page.extract_text()
            if extract:
                text += extract + "\n"
        return text

    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError(f"Formato não suportado: {path}")

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def smart_chunk(text, chunk_size, overlap):
    if not text:
        return []
        
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(text)
    chunks = []
    
    if len(tokens) == 0:
        return []

    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunk_text = encoder.decode(chunk_tokens)
        chunks.append(chunk_text)
        
        # Advance the start position
        # If we reached the end, break
        if end >= len(tokens):
            break
            
        start = end - overlap
        
        # Safety check to prevent infinite loops if overlap >= chunk_size
        if start >= end:
            start = end

    return chunks

def process_file(path, chunk_size, overlap):
    try:
        text = extract_text(path)
        text = clean_text(text)
        chunks = smart_chunk(text, chunk_size, overlap)
        return chunks
    except Exception as e:
        print(f"Erro ao processar arquivo {path}: {e}")
        return []
