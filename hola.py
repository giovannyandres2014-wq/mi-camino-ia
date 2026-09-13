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

# ============================================
# EJERCICIO DE PRACTICA 1
# ============================================

productos = ["Saltin" , "Festival", "Waffer" , "Tosh" ]
cantidades = [50, 30, 0, 15]
for producto, cantidad in zip(productos, cantidades):
    if cantidad > 0:
        print("Material", producto , ":" ,cantidad , "Unidades")
    else:
        print("Material", producto , ":" ,cantidad , "Agotado")

# ============================================
# TEMA 7: Funciones (empaquetar código para reutilizarlo)
# ============================================

# Definimos la función con "def", le damos un nombre, y un parámetro
# "edad" es el dato que la función va a recibir cada vez que la llamemos
def verificar_edad(edad):
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres Menor de Edad")

# Llamamos la función pasándole distintos valores
# Cada llamada usa el mismo código de adentro, pero con un dato diferente
verificar_edad(15)
verificar_edad(30)

# ============================================
# TEMA 8: Funciones con return (devuelven un valor)
# ============================================

# A diferencia de print (que solo muestra el resultado),
# "return" entrega el valor calculado para poder guardarlo y reutilizarlo
def calcular_total(cantidad1, cantidad2):
    total = cantidad1 + cantidad2
    return total

# Guardamos en una variable lo que la función devolvió
resultado = calcular_total(50, 30)
print("El total es:", resultado)