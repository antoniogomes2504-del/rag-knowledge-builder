
import json
import os

def export_to_markdown(chunks, base_filename, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_path = os.path.join(output_dir, f"{base_filename}_rag.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# Knowledge Base: {base_filename}\n\n")
        for i, chunk in enumerate(chunks):
            f.write(f"## Chunk {i+1}\n\n{chunk}\n\n---\n\n")
            
    return file_path

def export_to_json(chunks, base_filename, output_dir="output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    file_path = os.path.join(output_dir, f"{base_filename}_rag.json")
    
    data = []
    for i, chunk in enumerate(chunks):
        data.append({
            "chunk_id": i+1,
            "filename": base_filename,
            "content": chunk
        })
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    return file_path
