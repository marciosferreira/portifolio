import json
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = "gemini-3.5-flash"
CONTEXT_PATH = Path(__file__).parent / "marcio_context.md"

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY não definida. Configure no arquivo .env.")

MARCIO_CONTEXT = CONTEXT_PATH.read_text(encoding="utf-8")

SYSTEM_INSTRUCTION = f"""Você é o assistente do portfólio de Marcio Soares Ferreira.
Sua missão é responder perguntas de recrutadores, lideranças técnicas e potenciais
parceiros sobre o background, experiência, projetos e habilidades de Marcio.

REGRAS:
- Responda SEMPRE em português brasileiro, a menos que a pergunta seja feita em outro idioma.
- Seja conciso e direto — no máximo 3-4 parágrafos curtos, ou listas quando apropriado.
- Use APENAS as informações do contexto abaixo. Se a pergunta for sobre algo não
  documentado, diga educadamente que não tem essa informação e sugira contatar
  Marcio pelo LinkedIn ou e-mail.
- Nunca invente datas, números, métricas, projetos ou afiliações.
- Use linguagem profissional mas calorosa — você representa o Marcio.
- Se a pergunta for off-topic (não relacionada ao Marcio ou à carreira dele),
  redirecione com gentileza.
- Quando relevante, sugira links concretos (LinkedIn, GitHub, YouTube, demos).

FORMATAÇÃO (Markdown):
- SEMPRE formate as respostas em Markdown limpo e legível.
- Use **negrito** para destacar empresas, tecnologias, cargos, métricas e nomes próprios.
- Use listas com `-` para enumerar experiências, projetos, skills ou bullets.
- Use parágrafos curtos separados por linha em branco para melhorar a leitura.
- Use links Markdown `[texto](url)` quando citar LinkedIn, GitHub, demos ou publicações.
- Evite títulos grandes (`#`, `##`) — o chat é compacto. Prefira negrito quando precisar de ênfase de seção.
- Use `código inline` apenas para nomes de arquivos, comandos ou trechos técnicos curtos.

CONTEXTO SOBRE MARCIO (fonte da verdade):
---
{MARCIO_CONTEXT}
---
"""

client = genai.Client(api_key=GEMINI_API_KEY)

app = FastAPI()


class ChatRequest(BaseModel):
    question: str
    history: list[dict] | None = None


@app.post("/api/chat")
async def chat(req: ChatRequest):
    question = (req.question or "").strip()
    if not question:
        raise HTTPException(status_code=400, detail="Pergunta vazia.")

    contents = []
    for msg in (req.history or [])[-10:]:
        role = msg.get("role")
        text = (msg.get("text") or "").strip()
        if role not in ("user", "model") or not text:
            continue
        contents.append(types.Content(role=role, parts=[types.Part(text=text)]))
    contents.append(types.Content(role="user", parts=[types.Part(text=question)]))

    def event_stream():
        try:
            stream = client.models.generate_content_stream(
                model=MODEL_ID,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.4,
                    max_output_tokens=2000,
                    thinking_config=types.ThinkingConfig(thinking_level="minimal"),
                ),
            )
            for chunk in stream:
                text = getattr(chunk, "text", None)
                if text:
                    yield f"data: {json.dumps({'text': text})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


app.mount("/", StaticFiles(directory=".", html=True), name="static")
