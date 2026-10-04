"""
crear_estructura.py
Crea la estructura de carpetas del curso AI-Agent-Path, organizada por
módulo y semana, para ubicarte fácil cada vez que retomas el curso.

Cómo usarlo:
1. Copia este archivo dentro de tu carpeta AI-Agent-Path.
2. Ábrelo en VS Code y corre el script (o desde la terminal: python crear_estructura.py).
3. Va a crear todas las carpetas vacías listas para que muevas tus archivos.
"""

import os

# Estructura: carpeta de módulo -> lista de carpetas de semana
estructura = {
    "Modulo_1_Python": ["Semana_1", "Semana_2", "Semana_3", "Semana_4"],
    "Modulo_2_LLM_Prompting": ["Semana_5", "Semana_6", "Semana_7"],
    "Mini_Modulo_Seguridad": [],
    "Modulo_3_Agentes": ["Semana_8", "Semana_9", "Semana_10", "Semana_11", "Semana_12"],
}

carpeta_base = os.getcwd()  # asume que corres el script desde dentro de AI-Agent-Path

for modulo, semanas in estructura.items():
    ruta_modulo = os.path.join(carpeta_base, modulo)
    os.makedirs(ruta_modulo, exist_ok=True)
    print(f"Creada: {ruta_modulo}")

    for semana in semanas:
        ruta_semana = os.path.join(ruta_modulo, semana)
        os.makedirs(ruta_semana, exist_ok=True)
        print(f"  Creada: {ruta_semana}")

print("\nListo. Estructura de carpetas creada.")
print("Recuerda mover tus archivos .py y .xlsx existentes a la carpeta de semana que les corresponda.")
