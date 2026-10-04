import pandas as pd
import requests

STOCK_OBJETIVO = 20

# Pasos 1 y 2: cargar y limpiar
df = pd.read_excel("inventario.xlsx")
df = df[df["Producto"] != "TOTAL"]

# Paso 3: filtrar agotados
agotados = df[df["Cantidad"] == 0].copy()

# Paso 4: traer la TRM protegida
url = "https://www.datos.gov.co/resource/32sa-8pi3.json?$limit=1&$order=vigenciadesde DESC"

try:
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    trm = float(datos[0]["valor"])
    print(f"TRM del día: ${trm:,.2f} COP")
except Exception as error:
    print(f"No se pudo obtener la TRM: {error}")
    exit()

# Paso 5: calcular la reposición
agotados["Unidades a reponer"] = STOCK_OBJETIVO - agotados["Cantidad"]
agotados["Costo USD"] = agotados["Unidades a reponer"] * agotados["Precio Un"]
agotados["Costo COP"] = agotados["Costo USD"] * trm

print(agotados)

# Paso 6: armar y exportar el reporte
columnas = ["Producto", "Cantidad", "Precio Un", "Unidades a reponer", "Costo USD", "Costo COP"]
reporte = agotados[columnas].round(2)

#  Index=False le dice a pandas que no guarde la columna de numeracion en el excel    Producto  Cantidad  ...
# 0 1 2 3

reporte.to_excel("agotados_reporte.xlsx", index=False) 



total_cop = reporte["Costo COP"].sum()
print(f"Productos agotados: {len(reporte)}")
print(f"Costo total de reposición: ${total_cop:,.0f} COP")
print("Reporte guardado en agotados_reporte.xlsx")