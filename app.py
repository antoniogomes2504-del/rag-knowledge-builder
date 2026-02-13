
import streamlit as st
import os
import shutil
from src.processor import process_file
from src.utils import export_to_markdown, export_to_json

st.set_page_config(page_title="RAG Knowledge Builder", layout="wide")

st.title("🧠 RAG Knowledge Builder - Squad IA")

st.info("Ferramenta interna para preparação de datasets RAG.")

# Sidebar configuration
st.sidebar.header("Configurações")

with st.sidebar.expander("ℹ️ O que é Chunk Size?", expanded=False):
    st.markdown("""
    **Tamanho do bloco de texto** lido por vez.
    - **Muito pequeno:** Perde contexto.
    - **Muito grande:** Mistura assuntos.
    - *Recomendado: 500-800*
    """)

chunk_size = st.sidebar.slider("Chunk size (tokens)", 100, 2000, 700)

with st.sidebar.expander("ℹ️ O que é Overlap?", expanded=False):
    st.markdown("""
    **Sobreposição entre blocos** para não cortar frases.
    - Garante continuidade.
    - *Recomendado: 10-20% do tamanho*
    """)

overlap = st.sidebar.slider("Overlap (tokens)", 0, 500, 100)

uploaded_files = st.file_uploader(
    "Envie arquivos (.docx, .pdf, .txt)",
    type=["docx", "pdf", "txt"],
    accept_multiple_files=True
)

if "processed_data" not in st.session_state:
    st.session_state.processed_data = {}

if st.button("Processar Arquivos"):
    if not uploaded_files:
        st.warning("Envie pelo menos um arquivo.")
    else:
        # Create temp dir
        temp_dir = "temp_uploads"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        processed_count = 0
        total_files = len(uploaded_files)

        for i, file in enumerate(uploaded_files):
            status_text.text(f"Processando {file.name}...")
            
            # Save uploaded file temporarily
            temp_path = os.path.join(temp_dir, file.name)
            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())

            # Process
            chunks = process_file(temp_path, chunk_size, overlap)
            st.session_state.processed_data[file.name] = chunks
            
            # Update progress
            progress_bar.progress((i + 1) / total_files)
            
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
        status_text.success("Processamento concluído!")
        
        # Cleanup temp dir
        if os.path.exists(temp_dir):
            try:
                os.rmdir(temp_dir)
            except:
                pass # Directory might not be empty if something failed, ignore

# Display Results
if st.session_state.processed_data:
    st.markdown("---")
    st.subheader("📊 Resultados e Exportação")
    
    for filename, chunks in st.session_state.processed_data.items():
        with st.expander(f"📄 {filename} ({len(chunks)} chunks)"):
            st.write(f"**Total de chunks:** {len(chunks)}")
            
            # Preview first 3 chunks
            for i, chunk in enumerate(chunks[:3]):
                st.markdown(f"**Chunk {i+1} Preview:**")
                st.info(chunk[:500] + "..." if len(chunk) > 500 else chunk)

            # Export Logic
            col1, col2 = st.columns(2)
            
            # Generate exports on the fly for download buttons
            # Note: In a real app we might want to cache these or save to disk first
            # We'll use the utils to save to disk then read back for download
            
            md_path = export_to_markdown(chunks, os.path.splitext(filename)[0])
            json_path = export_to_json(chunks, os.path.splitext(filename)[0])
            
            with open(md_path, "r", encoding="utf-8") as f:
                md_data = f.read()
            
            with open(json_path, "r", encoding="utf-8") as f:
                json_data = f.read()

            with col1:
                st.download_button(
                    label="📥 Baixar Markdown",
                    data=md_data,
                    file_name=f"{filename}_rag.md",
                    mime="text/markdown",
                    key=f"dl_md_{filename}"
                )
            
            with col2:
                st.download_button(
                    label="📥 Baixar JSON",
                    data=json_data,
                    file_name=f"{filename}_rag.json",
                    mime="application/json",
                    key=f"dl_json_{filename}"
                )

