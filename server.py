import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request, send_from_directory, stream_with_context
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
    api_key=os.getenv("OLLAMA_API_KEY", "ollama"),
)
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


@app.get("/")
def index():
    return send_from_directory(BASE_DIR / "public", "index.html")


@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    messages = data.get("messages")
    if not isinstance(messages, list):
        return jsonify(error="Envie uma lista de mensagens."), 400

    @stream_with_context
    def generate():
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=True,
            )
            for chunk in stream:
                text = chunk.choices[0].delta.content
                if text:
                    yield text
        except Exception:
            app.logger.exception("Erro ao consultar o Ollama")
            yield f"\n\n[Erro: confira se o Ollama está rodando e se o modelo {MODEL} foi baixado.]"

    return Response(generate(), mimetype="text/plain; charset=utf-8", headers={"Cache-Control": "no-cache"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "3000"))
    print(f"Chatbot disponível em http://localhost:{port}")
    app.run(host="127.0.0.1", port=port, threaded=True)
