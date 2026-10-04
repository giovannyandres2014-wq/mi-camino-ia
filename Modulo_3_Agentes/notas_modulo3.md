# Notas — Módulo 3: Frameworks de Agentes y Function Calling (Semanas 8-12)

## Semana 8 — Qué es un agente y qué es function calling

Un AGENTE es un LLM al que se le da acceso a herramientas (funciones)
para que, además de hablar, pueda ACTUAR: consultar una API, leer un
archivo, hacer un cálculo. Esto es la diferencia clave con el Módulo 2,
donde el modelo solo generaba texto a partir del prompt.

FUNCTION CALLING es el mecanismo por el cual el modelo decide "necesito
usar esta herramienta" y te lo devuelve de forma estructurada (nombre
de la función + parámetros). El modelo NUNCA ejecuta código directamente
— "el modelo propone, tu código dispone". Tu programa en Python es el
que decide si de verdad ejecuta esa función.

Comparación con SAP: una tool se parece a una BAPI — una función de
negocio bien definida, con nombre y parámetros de entrada/salida claros.
La diferencia es que en function calling, es el MODELO quien decide
cuándo invocarla según el lenguaje natural del usuario, no un programa
con secuencia fija.

El protocolo de function calling ya lo da el SDK de Anthropic/OpenAI.
Las tools específicas del negocio (leer inventario, consultar TRM) las
escribe uno mismo, usando pandas por dentro como siempre — pandas hace
el trabajo de datos, function calling es la capa que conecta eso con
el modelo.

## Semana 9 — Diseñando herramientas (tools) para un agente

Principio: UNA TOOL, UNA RESPONSABILIDAD. Mejor varias tools pequeñas
y específicas (consultar_agotados, calcular_reposicion, consultar_trm)
que una sola función gigante que hace de todo.

La DESCRIPCIÓN en texto es lo único que el modelo realmente lee (no tu
código). Entre más clara y específica, mejor elige el modelo cuándo
usar cada tool.

Parámetros con restricciones claras (tipos, rangos válidos) como
primera línea de defensa de seguridad.

Regla de oro: NUNCA confiar ciegamente en lo que pide el modelo —
siempre validar los parámetros antes de ejecutar, igual que cualquier
input humano.

PRINCIPIO DE MENOR PRIVILEGIO: cada tool debe poder hacer solo lo
mínimo necesario (ej. una tool de solo lectura si no necesita escribir
o borrar nada).

## Semana 10 — Ciclo completo del agente

El ciclo de 5 pasos:
1. El usuario pregunta (lenguaje natural).
2. Se le manda la pregunta + la lista de tools disponibles al modelo.
3. El modelo responde pidiendo usar una o más tools (no da texto final
   todavía).
4. El código Python ejecuta esas funciones reales (pandas, API de TRM).
5. Se le devuelven los resultados reales al modelo, y ahí sí arma la
   respuesta final en lenguaje natural.

Técnicamente esto es un BUCLE (while), no una sola llamada: se repite
mientras el modelo siga pidiendo tools, hasta que devuelve una
respuesta de texto normal.

Caso de uso propio: agente con tools `consultar_agotados` y
`consultar_trm` sobre inventario.xlsx.

Pendiente: escribir el código real de este ciclo completo.

## Script construido — chatbot_inventario.py (Semana 6-8)
Chatbot con restricción de tema: se le mete el inventario completo como
contexto dentro del system prompt, y se le instruye que rechace con una
respuesta fija cualquier pregunta que no sea sobre ese inventario. Corre
en un bucle (while) para chatear varias veces sin reiniciar el script.
Base conceptual: el caso del compañero en EE.UU. que hizo algo similar
con Gemini ("solo responde sobre este archivo").

## Semana 11 — Frameworks (LangChain o similar) vs hacerlo a mano

Un FRAMEWORK es un conjunto de herramientas y reglas ya armadas que dan
una estructura para construir algo, en vez de empezar desde cero (pandas
es, en ese sentido, un framework para datos).

LANGCHAIN es un framework enfocado en construir aplicaciones con LLMs y
agentes: ya trae resuelto el bucle "pregunta → decide tool → ejecuta →
responde", conectores listos (PDFs, bases de datos, páginas web), memoria
de conversación entre turnos, y una forma estándar de definir tools que
funciona igual sin importar el modelo (Claude, GPT, etc.).

Ventaja: si cambia el proveedor de modelo, el cambio es mínimo porque la
lógica del agente está desacoplada del proveedor. Ahorra tiempo en piezas
genéricas (memoria, conectores).

Desventaja: añade una capa de abstracción — más que aprender, y más
difícil depurar cuando algo falla (no siempre se sabe si el problema es
del código propio o de cómo el framework actúa por detrás).

Recomendación para proyectos pequeños y específicos (como el agente de
inventario + TRM): construirlo a mano primero para afianzar fundamentos;
considerar LangChain cuando el proyecto crezca (múltiples tools, memoria
larga, varias fuentes de datos a la vez).

### Nota sobre Microsoft 365 / Copilot Studio
Dado que Grupo Nutresa migra a M365 en diciembre de 2026, el mismo agente
construido en Python se puede conectar con Copilot Studio: se expone el
agente de Python como una API propia (corriendo en un servidor, ej. Azure),
y en Copilot Studio se define una "acción personalizada" que llama a esa
API externa. Así, el usuario final interactúa con la interfaz de Microsoft
(Teams, chat de Copilot), pero la lógica real — validaciones, checklist de
seguridad, conexión a SAP o Excels — sigue corriendo en el código propio.
El concepto de fondo (rol, restricciones, tools, seguridad) es el mismo,
solo cambia si se implementa en código puro o en una interfaz visual como
Copilot Studio.

## Semana 12 — Proyecto final

Objetivo: convertir el chatbot con restricción de tema en un AGENTE real
con tools, usando el ciclo completo de la Semana 10, en vez de pegar todo
el inventario fijo en el system prompt.

Alcance propuesto: dos tools — `consultar_inventario` (filtra por agotados
o bajo stock según lo que pida el usuario) y `consultar_trm` (trae el
valor del dólar del día). El agente decide solo cuáles usar y en qué
orden según la pregunta.

Por qué es mejor que el chatbot anterior: el chatbot mete todo el
inventario como texto fijo (no escala con archivos grandes); con tools,
el agente solo pide los datos exactos que necesita en cada pregunta —
más eficiente en tokens y más parecido a un caso real de producción.

Entregable final: `agente_abastecimiento.py` — las dos tools definidas,
el bucle del ciclo del agente, validación de parámetros antes de ejecutar
cada tool, manejo de errores si la API de TRM falla, y la API key nunca
expuesta en el código (uso de .env).

Pendiente: escribir el código completo de este proyecto final.
