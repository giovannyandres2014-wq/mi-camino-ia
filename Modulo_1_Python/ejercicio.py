# Con esto, tu mapa mental queda completo y así:

#   1 Abrir ejercicio.py dentro de AI-Agent-Path.
#   2 Importar pandas.
#   3 Leer inventario.xlsx con pd.read_excel(...).
#4 Llamar una API que traiga el valor actual del dólar (USD→COP) y guardarlo en una variable.
#5 Crear la columna "Precio" (en dólares), según el nombre del producto (Saltín=1, Festival=2, Wafer=3, Tosh=4).
#6 Crear la columna "Precio total" = Cantidad × Precio × Valor del dólar.
#6 Sumar toda la columna "Precio total" para obtener el gran total.
#7 Agregar una fila extra al final de la tabla con ese total (por ejemplo, en la columna "Producto" diría "TOTAL", y en "Precio total" iría la suma).
#8 Guardar todo sobrescribiendo inventario.xlsx.

import pandas as pd
datos = pd.read_excel("inventario.xlsx")

import requests
respuesta = requests.get("https://open.er-api.com/v6/latest/USD")
datos_api = respuesta.json()
valor_dolar = datos_api["rates"]["COP"]

def asignar_precio(producto):
    if producto == "Saltin":
        return 1
    elif producto == "Festival":
        return 2
    elif producto == "Waffer":
        return 3
    elif producto == "Tosh":
        return 4

datos["Precio Un"] = datos["Producto"].apply(asignar_precio)
datos["Precio Total"] = datos["Cantidad"] * datos["Precio Un"] * valor_dolar
resumen = datos["Precio Total"].sum()
print(datos)
print(resumen)
fila_total = pd.DataFrame([{"Producto": "TOTAL", "Precio Total": resumen}])
datos = pd.concat([datos, fila_total], ignore_index=True)
datos.to_excel("inventario.xlsx", index=False)