# Notas — Módulo 1: Python Aplicado (Semanas 1-4)

## Resumen general
Fundamentos de Python, pandas para manejo de datos, y requests para
consumir APIs públicas. Cierra con un ejercicio integrador que junta
las tres piezas.

## Scripts de referencia (ya construidos)
- hola.py — primer script de prueba, confirma que el entorno está bien
  instalado (Semana 1)
- pandas_intro.py — leer un Excel con pandas, guardar resultados en Excel
  (Semana 1-2)
- inventario.py — crear un archivo de Excel con openpyxl (Semana 1-2)
- agrupar_datos.py — filtrar y agrupar datos con pandas (groupby),
  contar agotados y bajo stock (Semana 2-3)
- api_intro.py — primera petición a una API con requests: import requests,
  hacer peticiones, convertir la respuesta a JSON, enviar parámetros
  a una API (Semana 3)
- ejercicio.py — ejercicio integrador: lee inventario.xlsx, llama la API
  de TRM (USD→COP), crea columna "Precio" según el producto, crea columna
  "Precio Total" = Cantidad × Precio × Valor del dólar, suma el gran total,
  agrega fila TOTAL, guarda sobrescribiendo el Excel (Semana 4 — cierre
  del módulo)

## Correcciones importantes revisadas sobre ejercicio.py
- Verificar que el nombre del producto coincida exactamente con el Excel
  (ej. "Wafer" vs "Waffer" — un typo así da NaN en silencio, sin error)
- Usar un diccionario de precios en vez de cadenas de if/elif
- Lanzar un error claro (ValueError) si aparece un producto sin precio
  definido, en vez de fallar en silencio
- Filtrar cualquier fila "TOTAL" existente al inicio, para que el script
  se pueda correr varias veces sin acumular errores
- Usar raise_for_status() en la llamada a la API para detectar fallos
  de forma clara

## Ejercicios de refuerzo pendientes (antes de dar el módulo por cerrado)
- Ejercicio A: filtrado con pandas — contar agotados, contar bajo stock
  (Cantidad < 10), agrupar con groupby() por alguna categoría
- Ejercicio B: construir un DataFrame desde cero (diccionario → pd.DataFrame),
  agregar columna calculada, guardar como Excel
- Ejercicio C: manejo de errores con requests — try/except, raise_for_status(),
  romper la URL a propósito y capturar el error con un mensaje amigable

## Mini-proyecto de cierre del módulo (pendiente)
agotados_reporte.xlsx: lee inventario, filtra productos agotados,
llama la API de TRM, calcula cuánto costaría reponer una cantidad de
referencia (ej. 100 unidades) en COP por producto agotado, guarda un
nuevo Excel con: producto, precio unitario USD, valor del dólar del día,
costo estimado de reposición en COP.
