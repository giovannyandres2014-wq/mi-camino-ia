# Guía de modelos de IA — ¿cuál usar para qué?

*Actualizada: octubre 2026. Los modelos cambian seguido: antes de usar uno en producción, verifica el nombre exacto en la documentación oficial del proveedor.*

**Regla de oro:** usa el modelo más barato que haga bien la tarea. Arranca con el económico y sube solo si se queda corto.

Costo relativo: 💲 muy barato · 💲💲 medio · 💲💲💲 caro · 💲💲💲💲 premium

---

## Anthropic (Claude) — tu API key actual

| Modelo | Nombre en el código (`model=`) | Costo | Recomendado para |
|---|---|---|---|
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | 💲 | Chatbots de atención al cliente, clasificar textos, respuestas rápidas, tareas repetitivas de alto volumen. **Tu punto de partida para practicar.** |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 💲💲 | El equilibrio: agentes, código, análisis de documentos, extracción de datos de facturas, la mayoría de automatizaciones de negocio. |
| Claude Opus 5.5 | `claude-opus-5-5` | 💲💲💲 | Razonamiento complejo, análisis delicados donde un error sale caro (ej. conciliaciones críticas), tareas largas de varios pasos. |
| Claude Fable 5.1 | `claude-fable-5-1` | 💲💲💲💲 | Gama más alta. Solo para retos muy difíciles; casi nunca necesario para automatizaciones normales. |

## OpenAI (GPT)

| Modelo | Nombre en el código | Costo | Recomendado para |
|---|---|---|---|
| GPT-6 Luna | `gpt-6-luna` | 💲 | Tareas de alto volumen y bajo costo, chatbots sencillos. |
| GPT-6.1 Sol | `gpt-6.1-sol` | 💲💲 | Equilibrio entre inteligencia y costo. |
| GPT-6 Astra | (ver docs de OpenAI) | 💲💲💲 | Su modelo insignia: razonamiento complejo y código. |

## Google (Gemini)

| Modelo | Nombre en el código | Costo | Recomendado para |
|---|---|---|---|
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | 💲 | Muy barato y rápido; tareas simples y de alto volumen. |
| Gemini 3.8 Flash | `gemini-3.8-flash` | 💲💲 | Caballo de batalla: agentes, código, flujos de varios pasos. |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | 💲💲💲 | Tareas complejas y razonamiento avanzado (aún en preview). |

## Modelos de código abierto (los descargas y corres tú)

| Familia | Creador | Costo | Recomendado para |
|---|---|---|---|
| Llama | Meta | Gratis por token (pagas hardware/servidor) | Datos muy sensibles que no pueden salir de tu infraestructura. |
| DeepSeek | DeepSeek (China) | Gratis local / API muy barata | Bajo costo. Ojo con la privacidad si usas su API en la nube. |
| Qwen | Alibaba (China) | Gratis local / API barata | Igual que DeepSeek. |

---

## Guía rápida por caso de uso

| Si quieres... | Usa |
|---|---|
| Chatbot de atención al cliente | Haiku / GPT-6 Luna / Gemini Flash-Lite |
| Resumir, traducir, redactar correos | Haiku o Sonnet |
| Extraer datos de facturas o documentos | Sonnet |
| Agente que usa herramientas y toma decisiones | Sonnet (Opus si es muy complejo) |
| Análisis crítico donde un error cuesta mucho | Opus |
| Datos confidenciales sin salir de la empresa | Modelo abierto en servidor propio, o Claude vía Bedrock / Vertex / Azure según la nube de la empresa |

## Recordatorios

- Una sola API key sirve para **todos** los modelos de ese proveedor: el modelo lo eliges en la línea `model=` de tu código.
- Ponle límite de gasto a tu cuenta y deja apagada la recarga automática mientras practicas.
- No amarres tu código a un solo proveedor: así puedes cambiar de modelo según precio y calidad para cada cliente.

Documentación oficial: [Anthropic](https://docs.claude.com) · [OpenAI](https://developers.openai.com/api/docs/models) · [Google Gemini](https://ai.google.dev/gemini-api/docs)
