# ============================================
# TEMA 1: Variables y tipos de datos
# ============================================
nombre = "GIO"
edad = 15
es_programador = True

print("Hola, voy a ser AI Agent Engineer")
print("Estoy aprendiendo git hub")
print("Me llamo", nombre)
print("Mi edad es", edad)
print("Soy Programador?", es_programador)


# ============================================
# TEMA 2: Condicionales (if / else)
# ============================================
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres Menor de Edad")


# ============================================
# TEMA 3: Bucle for con range
# ============================================
for numero in range(1, 6):
    print(numero)


# ============================================
# TEMA 4: Listas y for básico
# ============================================
productos = ["galletas", "chocolatina", "pasabocas"]

for producto in productos:
    print("Producto:", producto)


# ============================================
# TEMA 5: Listas con enumerate (numerar mientras recorres)
# ============================================
bodegas = ["Vine", "Overland", "Treadway"]

for bodega in bodegas:
    print("bodega:", bodega)

for numero, bodega in enumerate(bodegas, start=1):
    print("Bodega", numero, ":", bodega)


# ============================================
# TEMA 6: Bucle while (se repite mientras se cumpla una condición)
# ============================================
inventario = 20

while inventario > 0:
    print("Quedan", inventario, "unidades")
    inventario = inventario - 5

print("Inventario agotado")