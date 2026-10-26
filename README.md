# Chatbot local com Python e Ollama

Chatbot web que responde em tempo real usando um modelo de linguagem executado no seu computador pelo Ollama.

## Requisitos

- Python 3.10 ou superior
- [Ollama](https://ollama.com/download)
- Modelo `llama3.2`

## Como executar no Windows

Abra o terminal do VS Code na pasta do projeto e execute estes comandos, um por vez:

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
~~~

Quando o servidor iniciar, abra [http://localhost:3000](http://localhost:3000) no navegador. Mantenha o Ollama e o terminal abertos enquanto usa o chatbot.

## Observação

Este projeto usa o Ollama no seu computador; não chama a API hospedada do ChatGPT. O GitHub armazena o código, mas não executa o chatbot.
  
