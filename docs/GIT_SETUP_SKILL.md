---
name: setup_corporate_git
description: Inicializa e envia um repositório Git em ambiente corporativo (bloqueio SSL), com criação manual no GitHub.
---

# Setup Git em Ambiente Corporativo

Use esta skill quando precisar subir um projeto local para o GitHub em um ambiente que intercepta conexões SSL (erro `SEC_E_UNTRUSTED_ROOT`) ou requer autenticação manual via browser.

## 1. Inicialização Local
Primeiro, garanta que o diretório é um repositório git.

```bash
git init
git add .
git commit -m "Initial commit"
```

## 2. Criação do Repositório Remoto (Ação Manual)
⚠️ **CRÍTICO:** O Git não pode criar o repositório remoto sozinho.
1. Peça ao usuário para criar um **repositório vazio** no GitHub (sem README, .gitignore ou License).
2. Peça a URL do novo repositório (ex: `https://github.com/USER/REPO.git`).

## 3. Configuração e Bypass de SSL
Configure o remoto e **desative a verificação SSL** para este projeto específico. Isso evita erros de certificado causados por proxies corporativos.

```bash
git remote add origin <URL_DO_REPOSITORIO>
git branch -M main
git config http.sslVerify false
```

## 4. Envio e Autenticação
Envie os arquivos. Isso deve abrir um pop-up de autenticação do Git Credential Manager ou pedir credenciais no terminal.

```bash
git push -u origin main
```

## 5. Verificação de Arquivos Ignorados
Se houver erro de arquivos faltando (ex: `requirements.txt` ignorado), force a adição:

```bash
git add -f <ARQUIVO_IGNORADO>
git commit -m "Fix: Forcing ignored file"
git push
```
