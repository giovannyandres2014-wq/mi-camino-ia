from dotenv import load_dotenv
import anthropic
import pandas as pd

load_dotenv()                     # Lee la llave desde .env
cliente = anthropic.Anthropic()   # Se conecta usando esa llave

# Paso 2: leer el reporte de agotados
df = pd.read_excel("agotados_reporte.xlsx")
print("Esto es lo que voy a enviarle a Claude:")
print(df)

# Paso 3: convertir la tabla en texto
tabla_texto = df.to_string(index=False)
print("\nAsí la va a leer Claude:")
print(tabla_texto)
# Paso 4: armar el prompt
prompt = f"""Eres un analista de abastecimiento de Galletas Noel.
Con base en este reporte de productos agotados, redacta una nota de alerta
breve para el jefe de compras. Incluye qué producto está agotado,
cuántas unidades reponer y el costo estimado en pesos y dólares.
Usa un tono profesional y directo, máximo 5 líneas.Copia los nombres de producto exactamente como aparecen en el reporte.
Escribe en texto plano, sin asteriscos ni formato markdown.

Reporte:
{tabla_texto}"""

print("\nPrompt que voy a enviar:")
print(prompt)

# Paso 5: enviar a Claude y recibir la nota
try:
    respuesta = cliente.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )
    nota = "".join(bloque.text for bloque in respuesta.content if bloque.type == "text")

    print("\n===== NOTA DE ALERTA =====")
    print(nota)
    print("Tokens:", respuesta.usage.input_tokens, "entrada /", respuesta.usage.output_tokens, "salida")

    # Guardar la nota en un archivo de texto
    with open("nota_alerta.txt", "w", encoding="utf-8") as archivo:
        archivo.write(nota)
    print("Nota guardada en nota_alerta.txt")

except Exception as error:
    print("No pude generar la nota:", error)