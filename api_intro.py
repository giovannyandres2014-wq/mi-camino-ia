# ============================================
# Primera peticion a una API con requests
# ============================================

import requests

# Hacemos una peticion GET a una API publica de prueba
respuesta = requests.get("https://api.github.com")

# Vemos el codigo de estado de la respuesta (200 significa que salio bien)
print("Codigo de estado:", respuesta.status_code)

# Vemos el contenido de la respuesta
print(respuesta.text)

# ============================================
# Convertir la respuesta a JSON (estructura de datos de Python)
# ============================================

datos_json = respuesta.json()

# Ahora podemos acceder a un valor especifico, como si fuera una cajita con nombre
print("URL de usuarios:", datos_json["user_url"])

# ============================================
# Enviar parametros a una API
# ============================================

parametros = {
    "latitude": 6.25,
    "longitude": -75.56,
    "current_weather": True
}

respuesta_clima = requests.get("https://api.open-meteo.com/v1/forecast", params=parametros)
datos_clima = respuesta_clima.json()

print(datos_clima)

clima_actual = datos_clima["current_weather"]

print("Temperatura actual:", clima_actual["temperature"], "grados")
print("Velocidad del viento:", clima_actual["windspeed"], "km/h")