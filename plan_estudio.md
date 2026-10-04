# Plan de Estudio — AI Agent Engineering (12 semanas)
Repositorio: mi-camino-ia

## Módulo 1 — Python aplicado (semanas 1-4)
- Fundamentos de Python, pandas, lectura/escritura de Excel
- Uso de requests para consumir APIs públicas
- Ejercicio integrador: inventario.xlsx + API de TRM (USD/COP)
- Pendiente: 3 ejercicios de refuerzo antes del mini-proyecto final
  - Ejercicio A: filtrado con pandas (agotados, bajo stock, groupby)
  - Ejercicio B: construir un DataFrame desde cero
  - Ejercicio C: manejo de errores con requests (try/except, raise_for_status)
- Mini-proyecto de cierre: agotados_reporte.xlsx (productos agotados + costo de reposición vía TRM)

## Módulo 2 — Fundamentos de LLM y prompting (semanas 5-7)
- Semana 5: cómo funciona un LLM (predicción de tokens), qué es un token,
  ventana de contexto, modelo base vs instruct/chat
- Semana 6: prompting efectivo — estructura (contexto + instrucción + formato),
  zero-shot vs few-shot, chain-of-thought, system vs user prompt, errores comunes
- Semana 7: uso de la API de Anthropic desde Python (SDK oficial),
  parámetros clave (model, max_tokens, temperature, system),
  manejo seguro de API keys (variables de entorno, nunca en el código)
- Ejercicio Semana 7: llm_inventario.py — lee inventario, filtra agotados,
  genera nota de alerta con el LLM

## Mini-módulo extra — Seguridad básica al usar IA para programar
- Origen: video sobre 20 errores comunes de seguridad en apps hechas con IA
- Conclusión clave: la seguridad real va en la arquitectura/scaffold,
  no solo en el prompt
- Checklist cubre: secretos (.env en gitignore), validación de permisos
  en servidor (no solo frontend), SQL parametrizado, RLS en base de datos,
  rate limiting, hash de contraseñas, tokens no en localStorage sin protección,
  validación de inputs y archivos subidos, no exponer stack trace en producción,
  dependencias actualizadas

## Módulo 3 — Frameworks de agentes y function calling (semanas 8-12)

### Semana 8 — Qué es un agente y qué es function calling (COMPLETADA - examen 100%)
- Un agente es un LLM con acceso a herramientas (funciones) para actuar,
  no solo responder con texto
- Function calling: el modelo decide qué herramienta necesita y te lo
  indica de forma estructurada; tu código es el que la ejecuta de verdad
- El modelo nunca ejecuta código directamente — "el modelo propone,
  tu código dispone"
- Comparación con SAP: una tool se parece a una BAPI (función de negocio
  bien definida, con nombre y parámetros claros). La diferencia es que
  en function calling es el MODELO quien decide cuándo invocarla, no un
  programa fijo
- El protocolo/mecanismo de function calling ya lo da el SDK de Anthropic/OpenAI;
  las tools específicas del negocio (leer inventario, consultar TRM) las
  escribe uno mismo, usando pandas por dentro como siempre

### Semana 9 — Diseñando herramientas (tools) para un agente
- Principio: una tool, una responsabilidad (evitar funciones gigantes
  que hacen de todo)
- La descripción en texto es lo que el modelo realmente lee — entre más
  clara y específica, mejor elige el modelo cuándo usarla
- Parámetros con restricciones claras (tipos, rangos válidos) como primera
  línea de defensa
- Regla de oro: nunca confiar ciegamente en lo que pide el modelo —
  siempre validar antes de ejecutar, igual que un input humano
- Principio de menor privilegio: cada tool hace solo lo mínimo necesario
  (ej. tool de solo lectura si no necesita escribir)

### Semana 10 — Ciclo completo del agente
- El ciclo de 5 pasos:    1) usuario pregunta, 2) se le manda la pregunta +
  lista de tools disponibles al modelo, 3) el modelo pide usar una o más
  tools (no responde texto aún), 4) el código ejecuta esas funciones reales
  (pandas, API de TRM), 5) se le devuelven los resultados reales al modelo
  y arma la respuesta final en lenguaje natural
- Técnicamente es un bucle (while) que se repite mientras el modelo siga
  pidiendo tools, hasta que devuelve una respuesta de texto normal
- Caso de uso propio: agente con tools `consultar_agotados` y `consultar_trm`
  sobre inventario.xlsx
- Pendiente: escribir el código real de este ciclo con las dos tools

### Semana 11 — Frameworks (LangChain o similar) vs hacerlo a mano
- Pendiente de ver

### Semana 12 — Proyecto final
- Agente aplicado a inventario + TRM + abastecimiento, con tools propias
  y checklist de seguridad aplicado
- Pendiente de ver
