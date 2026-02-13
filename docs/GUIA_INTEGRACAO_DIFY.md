# 🔌 Guia de Integração: RAG Tool + Dify

Este guia explica como configurar o **Dify** para aceitar os arquivos `.md` gerados pela nossa ferramenta, garantindo a melhor qualidade de resposta.

---

## Passo 1: Upload do Arquivo
1. No Dify, crie ou acesse uma Knowledge Base (Conhecimento).
2. Clique em **"Criar Conhecimento"** ou **"Adicionar Arquivo"**.
3. Faça o upload do arquivo `.md` que você baixou da nossa ferramenta.

---

## Passo 2: Configurações de Fragmentação (Sua 1ª Imagem) ⚙️

Como o arquivo já foi "cortado" (chunked) pela nossa ferramenta, devemos configurar o Dify para respeitar esses cortes.

1. **NÃO use "Pai-filho"**: Essa opção é complexa e tenta recriar estruturas que já fizemos.
2. Troque para a opção **"Personalizado"** (ou "Geral" / "Custom").
3. Configure assim:
   *   **Separador de Segmentos:** Digite `---`
       *   *Por que?* Nossa ferramenta insere `---` exatamente onde termina um bloco e começa outro. Isso força o Dify a usar nossos blocos perfeitos.
   *   **Comprimento Máximo:** Pode deixar `2000` (já controlamos isso na ferramenta).
   *   **Pré-processamento:** Desmarque "Substituir quebras de linha", pois nossos arquivos já estão limpos.

> **Resumo:** Queremos que o Dify seja apenas o "banco de dados", pois a "inteligência do corte" já foi feita pela nossa RAG Tool.

---

## Passo 3: Configuração de Recuperação (Sua 2ª Imagem) 🔎

Após clicar em "Salvar e Processar", você verá as configurações de busca.

1. **Modo de Pesquisa**:
   *   Escolha **Pesquisa Híbrida** (Recomendado se disponível).
   *   Se não tiver Rerank configurado, use **Pesquisa Vetorial** (Padrão).

2. **Parâmetros (Ajuste Fino)**:
   *   **Top K**: `3` a `5`
       *   *O que é?* Quantos pedaços de texto a IA vai ler para responder.
       *   *Dica:* Se a resposta precisa de muita informação, aumente para 5.
   *   **Limiar de Pontuação (Score/Threshold)**: `0.50` ou `0.60`
       *   *O que é?* O nível de exigência. Se for muito alto (0.8+), a IA pode dizer "não sei" se não achar algo idêntico. Se for muito baixo (0.3), ela pode alucinar com coisas nada a ver.
       *   *Recomendação:* Comece com **0.50** e suba se sentir que ela está trazendo lixo.

---

## Dica Final
Se estiver usando o modo **JSON** exportado pela ferramenta, você pode usar a opção de importação via **API** ou **Tabela** no Dify, mas o método `.md` descrito acima é o mais visual e simples para começar.
