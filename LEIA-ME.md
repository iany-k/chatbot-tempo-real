# Chatbot local com Python e Ollama

## Requisitos

- Python 3.10 ou superior
- Ollama instalado e o modelo `llama3.2` baixado

## Iniciar no Windows

Abra o PowerShell nesta pasta e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

Depois acesse http://localhost:3000. Mantenha o Ollama aberto enquanto usar o chatbot.

A configuração local fica no arquivo `.env`. O `.env.example` mostra os valores padrão; não publique o `.env` no GitHub.

