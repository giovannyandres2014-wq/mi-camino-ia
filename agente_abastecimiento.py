from dotenv import load_dotenv
import anthropic
import pandas as pd

load_dotenv()
cliente = anthropic.Anthropic()

# La "mano": busca un producto en el inventario
def consultar_inventario(producto):
    df = pd.read_excel("inventario.xlsx")
    fila = df[df["Producto"] == producto]

    if len(fila) == 0:
        return f"No encontré el producto {producto} en el inventario."

    cantidad = int(fila.iloc[0]["Cantidad"])
    if cantidad == 0:
        return f"{producto}: agotado, 0 unidades."
    else:
        return f"{producto}: {cantidad} unidades disponibles."

# Prueba rápida de la mano, sin Claude todavía
# El "catálogo": lo que Claude lee para decidir
herramientas = [
    {
        "name": "consultar_inventario",
        "description": "Consulta las unidades disponibles de un producto en el inventario de Galletas Noel. Úsala cuando pregunten por stock, existencias o agotados.",
        "input_schema": {
            "type": "object",
            "properties": {
                "producto": {"type": "string", "description": "Nombre exacto del producto, por ejemplo Waffer"}
            },
            "required": ["producto"]
        }
    }
]

# Los "nervios": leen la orden de Claude y mueven la mano correcta
def ejecutar_herramienta(nombre, entrada):
    if nombre == "consultar_inventario":
        return consultar_inventario(entrada["producto"])
    return f"Herramienta desconocida: {nombre}"

# La conversación arranca con la pregunta del usuario
instrucciones = """Eres el asistente de abastecimiento de Galletas Noel.
Responde en español, en texto plano, sin asteriscos ni formato markdown.
Sé breve y directo, como en un reporte de operación.
Copia los nombres de producto exactamente como aparecen en el inventario."""

pregunta = input("Pregunta: ")
mensajes = [{"role": "user", "content": pregunta}]

# El ciclo del agente
while True:
    respuesta = cliente.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        system=instrucciones,
        tools=herramientas,
        messages=mensajes
    )
    # Guardamos lo que Claude dijo para que recuerde la conversación
    mensajes.append({"role": "assistant", "content": respuesta.content})

    if respuesta.stop_reason == "tool_use":
        resultados = []
        for bloque in respuesta.content:
            if bloque.type == "tool_use":
                print(f"  [Claude pidió: {bloque.name} con {bloque.input}]")
                resultado = ejecutar_herramienta(bloque.name, bloque.input)
                resultados.append({
                    "type": "tool_result",
                    "tool_use_id": bloque.id,
                    "content": resultado
                })
        # Le devolvemos a Claude lo que trajo la mano
        mensajes.append({"role": "user", "content": resultados})
    else:
        break

# Respuesta final
nota = "".join(b.text for b in respuesta.content if b.type == "text")
print("\n" + nota)