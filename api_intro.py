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