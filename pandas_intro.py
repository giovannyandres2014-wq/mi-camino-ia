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

# ============================================
# Guardar el resultado en un nuevo archivo de Excel
# ============================================

datos.to_excel("inventario_procesado.xlsx", index=False)

print("Archivo procesado guardado con éxito")

# ============================================
# Ordenar los datos por cantidad
# ============================================

ordenado = datos.sort_values("Cantidad", ascending=False)
print("Inventario ordenado de mayor a menor cantidad:")
print(ordenado)

# ============================================
# Agrupar datos (como una tabla dinámica de Excel)
# ============================================

import pandas as pd

datos_categoria = pd.DataFrame({
    "Producto": ["Saltin", "Festival", "Waffer", "Tosh", "Ducales", "Noel"],
    "Categoria": ["Saladas", "Dulces", "Dulces", "Saladas", "Saladas", "Dulces"],
    "Cantidad": [50, 30, 0, 15, 40, 25]
})

resumen = datos_categoria.groupby("Categoria")["Cantidad"].sum()
print(resumen)

# ============================================
# Manejo de errores con try/except
# ============================================

try:
    archivo = pd.read_excel("archivo_que_no_existe.xlsx")
    print(archivo)
except:
    print("No se pudo leer el archivo, revisa que el nombre sea correcto")