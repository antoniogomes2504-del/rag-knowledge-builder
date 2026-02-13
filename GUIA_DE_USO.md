# 📘 Guia de Uso: RAG Knowledge Builder

Este guia explica como utilizar a ferramenta da squad para preparar documentos para Inteligência Artificial (RAG - Retrieval Augmented Generation).

---

## 🚀 Para que serve?

Quando queremos que uma IA (como GPT-4, Dify ou Claude) "leia" documentos grandes (manuais, contratos, relatórios), não podemos enviar o texto inteiro de uma vez só. Precisamos dividir esse texto em pedaços menores e organizados.

Esta ferramenta faz exatamente isso:
1.  Lê seus arquivos (.pdf, .docx, .txt).
2.  Limpa a "sujeira" (espaços extras, quebras de linha erradas).
3.  Divide o texto em blocos inteligentes (**Chunks**).
4.  Exporta pronto para ser importado no Dify ou outra base de conhecimento.

---

## ⚙️ Entendendo as Configurações

No menu lateral esquerdo, você verá duas barras de ajuste. Aqui está o que elas significam de forma simples:

### 1. Chunk Size (Tamanho do Bloco)
> *"Qual o tamanho da 'mordida' que a IA vai dar no texto?"*

*   Define quantos **tokens** (aproximadamente palavras/sílabas) cada pedaço de texto terá.
*   **Por que importa?** 
    *   Se for **muito pequeno**, a IA pode perder o contexto (ex: lê uma resposta sem saber a pergunta).
    *   Se for **muito grande**, a busca fica imprecisa e mistura muitos assuntos num bloco só.
*   **Recomendação:**
    *   Para **Dify / GPT-4**: `500` a `800` tokens é o ideal.
    *   Para respostas muito detalhadas: `1000` a `1200`.

### 2. Overlap (Sobreposição)
> *"Para não cortar uma frase no meio."*

*   Define quanto do final do *Bloco 1* será repetido no início do *Bloco 2*.
*   **Por que importa?** Imagine que uma frase importante está bem na divisa do corte. Sem overlap, metade da frase fica num bloco e metade no outro, e a IA não entende. Com overlap, a frase aparece completa em pelo menos um dos blocos.
*   **Recomendação:**
    *   Geralmente **10% a 20%** do tamanho do Chunk.
    *   Exemplo: Se Chunk Size é `700`, use Overlap de `70` a `100`.

### 3. Quando alterar as configurações? (Guia Prático)

| Situação | Ajuste Recomendado | Por quê? |
| :--- | :--- | :--- |
| **Padrão (Maioria dos casos)** | **700 / 100** | Funciona bem para manuais, artigos e textos gerais. |
| **Textos Complexos / Contratos** | **Aumentar Chunk (1000+)** | Se o documento tem parágrafos muito longos e a IA precisa ler "muito" para entender o contexto de uma cláusula. |
| **FAQ / Perguntas e Respostas** | **Diminuir Chunk (300-500)** | Se cada resposta é curta, um chunk grande pode misturar a "Resposta A" com a "Pergunta B", confundindo a IA. |
| **IA responde "pela metade"** | **Aumentar Overlap (150-200)** | Se a IA corta o raciocínio no meio, aumentar a repetição ajuda a conectar os pontos. |

---

## 👣 Passo a Passo

1.  **Arraste seus arquivos**: Na área cinza central, solte seus PDFs, Word ou arquivos de texto.
2.  **Ajuste as réguas** (opcional):
    *   Deixe em **700 / 100** para um padrão ótimo.
3.  **Clique em "Processar Arquivos"**.
4.  **Confira o Resultado**:
    *   O app vai mostrar quantos "pedaços" foram gerados.
    *   Você pode ler uma prévia para ver se o corte ficou bom.
5.  **Baixe o Resultado**:
    *   📥 **Baixar Markdown**: Ótimo para ler visualmente.
    *   📥 **Baixar JSON**: O formato perfeito para importar no Dify ou banco de dados vetorial.

---

## 💡 Dica de Ouro
Se você notar que a IA está respondendo coisas "pela metade", tente **aumentar o Overlap** para garantir que ela tenha mais contexto entre um parágrafo e outro.
