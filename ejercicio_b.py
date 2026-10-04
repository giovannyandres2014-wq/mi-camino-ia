import pandas as pd

datos = {
    "Producto": ["Saltin", "Festival", "Waffer", "Tosh", "Ducales"],
    "Cantidad": [50, 30, 0, 15, 8],
    "Precio Un": [1.0, 2.0, 3.0, 4.0, 2.5]
}

print(datos)
df = pd.DataFrame(datos)
print(df)
df["Precio Total"] = df["Cantidad"] * df["Precio Un"]
print(df)
df.to_excel("inventario_creado.xlsx", index=False)
print("Archivo guardado con éxito")