
# 🧠 RAG Knowledge Builder - Squad IA

Ferramenta interna para preparação de datasets RAG (Retrieval-Augmented Generation).

## Funcionalidades

- **Upload Múltiplo**: Suporta .docx, .pdf, .txt
- **Chunking Inteligente**: Configurável (tamanho do chunk e overlap)
- **Preview**: Visualização dos chunks antes da exportação
- **Exportação**: Markdown (.md) e JSON

## Como rodar localmente

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o app:
   ```bash
   streamlit run app.py
   ```

## Deploy no Streamlit Cloud

1. Faça o fork/push deste repositório para o seu GitHub.
2. Acesse [share.streamlit.io](https://share.streamlit.io/).
3. Clique em "New app".
4. Selecione o repositório e a branch `main`.
5. Aponte o `Main file path` para `app.py`.
6. Clique em "Deploy!".
