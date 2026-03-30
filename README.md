# 📄 LDO Cidadã 2025 → Markdown

> Conversão automatizada de PDF para Markdown com pós-processamento para melhoria de formatação.

---

## ✨ Visão geral

Este projeto realiza a conversão da **LDO Cidadã 2025** (PDF) para o formato **Markdown (.md)** utilizando uma API construída com FastAPI.

Além da conversão, foi desenvolvido um script em Python para **limpeza e organização automática do conteúdo**, melhorando a legibilidade do documento final.

---

## 🚀 Funcionalidades

✅ Upload de PDF
✅ Conversão automática para Markdown
✅ Geração de arquivo `.md`
✅ Script de limpeza e formatação
✅ Estrutura organizada para leitura

---

## 🛠️ Tecnologias

* 🐍 Python
* ⚡ FastAPI
* 🚀 Uvicorn
* 📝 MarkItDown

---

## 📂 Estrutura do projeto

```bash id="q9t1q2"
.
├── app.py              # API de conversão
├── limpar_md.py        # Script de limpeza
├── ldo.md              # Markdown bruto
├── ldo_final.md        # Markdown final (tratado)
├── requirements.txt
└── LDO-CIDADA-2025-1.pdf
```

---

## ▶️ Como executar

### 1. Clonar repositório

```bash id="a6k2fz"
git clone https://github.com/LorenadeCastro/ldo-markdown.git
cd ldo-markdown
```

---

### 2. Criar ambiente virtual

```bash id="3d9f7h"
python -m venv venv
```

Ativar:

```bash id="tw3m8x"
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash id="u1z7rq"
pip install -r requirements.txt
```

---

### 4. Rodar a API

```bash id="s5f0jk"
python -m uvicorn app:app --reload
```

👉 Acesse: http://127.0.0.1:8000/docs

---

## 🔄 Conversão do PDF

```bash id="u3c6lp"
curl -X POST "http://127.0.0.1:8000/convert" -F "file=@LDO-CIDADA-2025-1.pdf" -o resultado.json
```

---

## 📄 Gerar Markdown

```bash id="h9y2vd"
(Get-Content resultado.json | ConvertFrom-Json).markdown | Out-File ldo.md
```

---

## 🧹 Limpeza automática

```bash id="l4m8qs"
python limpar_md.py
```

👉 Resultado final:

```bash id="b0k1pn"
ldo_final.md
```

---

## 🎯 Resultado

O arquivo final apresenta:

* 📚 melhor organização
* 🧾 títulos estruturados
* 📌 listas formatadas
* 🧹 remoção de ruídos do PDF

---

## 📌 Observações

A conversão é automatizada e pode gerar pequenas inconsistências, que são tratadas no script de pós-processamento.

---

## 👩‍💻 Autora

**Lorena de Castro**

---

## ⭐ Extras

Se esse projeto te ajudou ou serviu como referência, considere deixar uma ⭐ no repositório!
