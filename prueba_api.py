from dotenv import load_dotenv
import anthropic

load_dotenv()                     # Lee la llave desde el archivo .env
cliente = anthropic.Anthropic()   # Se conecta usando esa llave

respuesta = cliente.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Saluda a Gio en una frase corta."}]
)

print(respuesta.content[0].text)
print("Tokens usados:", respuesta.usage.input_tokens, "entrada /", respuesta.usage.output_tokens, "salida")
