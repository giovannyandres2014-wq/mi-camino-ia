print("Hola, voy a ser AI Agent Engineer")
print("Estoy aprendiendo git hub")
nombre = "GIO"
edad = 15
es_programador = True


print("Me llamo" , nombre)
print("Mi edad es" , edad)
print("Soy Programador?" , es_programador)
if edad >= 18: print("Eres mayor de edad")
else:print("Eres Menor de Edad")
for numero in range(1, 6):
    print(numero)
    productos = ["galletas", "chocolatina", "pasabocas"]

for producto in productos:
    print("Producto:", producto)

bodegas = ["Vine", "Overland" , "Treadway"]
for bodega in bodegas:
    print("bodega:" ,bodega)

for numero, bodega in enumerate(bodegas, start=1):
    print("Bodega", numero, ":", bodega)
    inventario = 20

while inventario > 0:
    print("Quedan", inventario, "unidades")
    inventario = inventario - 5

print("Inventario agotado")