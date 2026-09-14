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