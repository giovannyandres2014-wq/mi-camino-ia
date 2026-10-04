import requests

url = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=1&$order=vigenciadesde DESC"

try:
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    trm = float(datos[0]["valor"])
    print(f"TRM del día: ${trm:,.2f} COP")
except Exception as error:
    print(f"No se pudo obtener la TRM: {error}")