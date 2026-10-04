# Notas — Módulo 2: Fundamentos de LLM y Prompting (Semanas 5-7)

## Semana 5 — Cómo funciona un LLM por dentro

Un LLM no busca información en una base de datos ni "sabe" cosas como una
persona. Lo que hace es predecir, token por token, cuál es la palabra o
fragmento más probable que sigue, dado todo el texto anterior. Por eso a
veces "alucina" con total seguridad: está prediciendo lo que suena
probable, no consultando una fuente de verdad.

Un TOKEN es un fragmento de texto (a veces una palabra completa, a veces
un pedazo de ella). Importa porque normalmente se paga por token
(entrada + salida de la API), y cada modelo tiene un máximo de tokens
que puede procesar a la vez.

La VENTANA DE CONTEXTO es el máximo de tokens que el modelo puede
tener en cuenta en un momento dado. Lo que queda fuera, simplemente
nunca lo "ve" — no es que lo olvide como una persona.

Un modelo BASE solo continúa patrones de texto. Un modelo
INSTRUCT/CHAT (como Claude) pasó por entrenamiento extra para
comportarse como asistente útil, entendiendo que debe responder
directo a lo que se le pregunta.

## Semana 6 — Prompting efectivo

Estructura de un buen prompt: CONTEXTO (quién eres, para qué es esto) +
INSTRUCCIÓN CLARA (qué exactamente quieres, con verbos específicos) +
FORMATO DE SALIDA esperado (lista, tabla, longitud máxima).

ZERO-SHOT: pides la tarea sin ejemplos, confiando en el entrenamiento
del modelo. FEW-SHOT: das 1-3 ejemplos de entrada→salida antes de tu
petición real, para que copie el patrón exacto.

CHAIN-OF-THOUGHT: para tareas con varios pasos de lógica, pedirle
explícitamente que "piense paso a paso" antes de dar la respuesta
final mejora la precisión.

SYSTEM PROMPT vs USER PROMPT: el system define el rol y las reglas
generales (se manda una vez); el user es la pregunta específica de
ese turno.

Errores comunes: ambigüedad en la instrucción, no definir restricciones
de formato/largo, y pedir demasiadas tareas distintas en un solo prompt.

## Semana 7 — De la API a la práctica

Se usa el SDK oficial de Anthropic (pip install anthropic) en vez de
requests a mano. Parámetros clave: `model` (qué modelo usar), `max_tokens`
(límite de la respuesta), `temperature` (0 = consistente/predecible,
ideal para tareas de trabajo; más alto = más creativo/variado), `system`
(el rol y reglas).

Seguridad: la API key NUNCA va escrita directo en el código. Se guarda
en un archivo `.env` (que está en `.gitignore`, nunca se sube a Git) y
se lee con `os.environ.get("ANTHROPIC_API_KEY")`.

Ejercicio de la semana: `llm_inventario.py` — lee el inventario con
pandas, filtra productos agotados, arma un texto con esa lista, y se
lo manda al LLM pidiéndole que redacte una nota de alerta para el
equipo de abastecimiento.

## Mini-módulo extra — Seguridad básica al usar IA para programar

Conclusión clave: la seguridad real va en la ARQUITECTURA/SCAFFOLD, no
solo en el prompt. Pedirle a la IA "hazlo seguro" no es suficiente;
hay que partir de buenas prácticas estructurales.

Checklist: `.env` en `.gitignore` (nunca subir secretos a Git), validar
permisos siempre en el SERVIDOR (nunca confiar solo en el frontend),
queries SQL parametrizadas (nunca concatenar texto), RLS activado en
bases de datos con info de usuarios, rate limiting en endpoints
públicos, contraseñas con hash (nunca texto plano), tokens de sesión
no en localStorage sin protección, validar todo input y archivo
subido, no mostrar stack trace completo en producción, dependencias
actualizadas.
