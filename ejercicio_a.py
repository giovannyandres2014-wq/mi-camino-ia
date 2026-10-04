import pandas as pd
df = pd.read_excel("inventario.xlsx")
df = df[df["Producto"] != "TOTAL"]
print(df)
agotados = df[df["Cantidad"] == 0]
print(agotados)
bajo_stock = df[(df["Cantidad"] > 0) & (df["Cantidad"] < 10)]
print(bajo_stock)
valor_total = df["Precio Total"].sum()
print(valor_total)
print("===== RESUMEN DE INVENTARIO =====")
print(f"Productos agotados: {len(agotados)}")
print(f"Productos en bajo stock: {len(bajo_stock)}")
print(f"Valor total del inventario: ${valor_total:,.0f} COP")