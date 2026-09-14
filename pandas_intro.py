# ============================================
# Leer un Excel con pandas
# ============================================

import pandas as pd

# Leemos el archivo de Excel completo, de una sola vez
datos = pd.read_excel("inventario.xlsx")

# Mostramos la tabla completa
print(datos)

total = datos["Cantidad"].sum()
print("Total de unidades en inventario:", total)
agotados = datos[datos["Cantidad"] == 0]
print("Productos agotados:")
print(agotados)

# ============================================
# Crear una columna nueva con una condición (como un SI de Excel) Cuando después usas .apply(estado_producto), 
# pandas toma esa función y la va llamando automáticamente para cada fila de tu columna "Cantidad", una por una, 
# como si tú mismo llamaras la función 4 veces seguidas (una por cada producto), 
# pero sin tener que escribir esas 4 llamadas a mano.
# ============================================

def estado_producto(cantidad):
    if cantidad == 0:
        return "Agotado"
    else:
        return "Disponible"

datos["Estado"] = datos["Cantidad"].apply(estado_producto)

print(datos)