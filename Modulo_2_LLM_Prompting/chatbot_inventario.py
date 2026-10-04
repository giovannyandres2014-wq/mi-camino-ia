"""
chatbot_inventario.py
Chatbot restringido: solo responde preguntas sobre el archivo inventario.xlsx.
Si el usuario pregunta algo fuera de ese tema, el modelo se niega a responder.

Idea basada en la conversación sobre el caso de un compañero con Gemini:
el system prompt define el ROL + una RESTRICCIÓN explícita de tema.

Antes de correrlo:
- pip install pandas anthropic python-dotenv openpyxl
- Archivo .env en la misma carpeta con: ANTHROPIC_API_KEY=tu-key-aqui
"""

import pandas as pd
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# --- Leer el inventario una sola vez al iniciar ---
datos = pd.read_excel("inventario.xlsx")
texto_inventario = datos.to_string(index=False)

# --- System prompt: rol + restricción de tema ---
system_prompt = (
    "Eres un asistente de abastecimiento. Solo puedes responder preguntas "
    "relacionadas con el siguiente inventario:\n\n"
    f"{texto_inventario}\n\n"
    "Si el usuario pregunta algo que no tiene relación con este inventario "
    "(por ejemplo temas personales, noticias, otros productos no listados, "
    "o cualquier tema ajeno al abastecimiento), responde exactamente: "
    "'Solo puedo responder preguntas relacionadas con este inventario.' "
    "No inventes información que no esté en los datos proporcionados."
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

print("Chatbot de inventario listo. Escribe 'salir' para terminar.\n")

# --- Bucle de conversación ---
while True:
    pregunta = input("Tú: ")

    if pregunta.lower() == "salir":
        print("Chatbot: ¡Hasta luego!")
        break

    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system=system_prompt,
        messages=[{"role": "user", "content": pregunta}],
    )

    print("Chatbot:", respuesta.content[0].text)
    print()
