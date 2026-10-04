"""
llm_inventario.py
Semana 7 — Conecta pandas con la API de Anthropic.

Qué hace:
1. Lee inventario.xlsx con pandas.
2. Filtra los productos agotados (Cantidad == 0).
3. Arma un texto con esa lista.
4. Le manda un prompt bien estructurado al LLM (contexto + instrucción + formato)
   pidiendo una nota de alerta para el equipo de abastecimiento.
5. Imprime la respuesta del modelo.

Antes de correrlo:
- pip install pandas anthropic python-dotenv openpyxl
- Crea un archivo .env (en la misma carpeta) con esta línea:
  ANTHROPIC_API_KEY=tu-key-aqui
- Asegúrate que .env esté en tu .gitignore (nunca se sube a Git)
"""

import pandas as pd
import anthropic
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env al entorno
load_dotenv()

# --- Paso 1: leer el inventario ---
datos = pd.read_excel("inventario.xlsx")

# --- Paso 2: filtrar agotados ---
agotados = datos[datos["Cantidad"] == 0]

if agotados.empty:
    print("No hay productos agotados. No se genera nota de alerta.")
else:
    # --- Paso 3: armar el texto con la lista de productos ---
    lista_productos = ", ".join(agotados["Producto"].tolist())

    # --- Paso 4: llamar al LLM con un prompt estructurado ---
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    respuesta = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system=(
            "Eres un asistente de abastecimiento. Respondes en español, "
            "de forma breve y profesional."
        ),
        messages=[
            {
                "role": "user",
                "content": (
                    f"Estos productos están agotados: {lista_productos}. "
                    "Redacta una nota corta (máximo 3 líneas) para el equipo "
                    "de abastecimiento, alertando que se deben reponer."
                ),
            }
        ],
    )

    # --- Paso 5: imprimir la respuesta ---
    nota = respuesta.content[0].text
    print("Productos agotados:", lista_productos)
    print()
    print("Nota generada:")
    print(nota)
