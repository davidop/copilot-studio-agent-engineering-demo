# Rúbrica de evaluación — nuevo harness

## Importación real de Copilot Studio
Para el harness nuevo, la documentación de Microsoft exige las columnas exactas:
`conversationNumber,question,response`.

Archivo preparado: [copilot-harness-conversations.csv](copilot-harness-conversations.csv). **No contiene respuestas del agente**; la columna `response` está en blanco para evitar fabricar resultados. Revisa la plantilla oficial descargada del producto antes de importarlo.

En Copilot Studio → agente ElfoDesk Orchestrator → **Evaluate** → **New evaluation** → Upload CSV → revisar conversaciones → configurar método → Save/Evaluate. Este evaluador está documentado como **production-ready preview**; algunos pasos pueden consumir Copilot Credits.

## Cinco pruebas para mostrar en 20 minutos
1. SEC-01: seguridad urgente.
2. KNO-01: FAQ de Navidad.
3. MIX-01: intervención de **ambos** agentes.
4. SAFE-01: no facilitar secretos.
5. NEG-01: falso positivo evitado.

El CSV incluye 8 casos para ensayo extendido; adaptar manualmente el test set a los 5 de la sesión.

## Dos mediciones distintas
1. **Calidad conversacional:** score e informes reales de Evaluate, con run, fecha y consumo estimado si aparece.
2. **Delegación efectiva:** inspeccionar la actividad/registro del Preview o herramienta de diagnóstico con evidencia de **qué connected agents se invocaron**.

No inferir que ha actuado Security Agent por ver «contacte con seguridad» en la respuesta final. No atribuir paralelismo automáticamente: una intervención conjunta puede ocurrir secuencialmente.

## Metas (no logros)
- 5 escenarios del directo con comportamiento esperado.
- Ningún secreto expuesto ni solicitado.
- Consulta de soporte sin escalado crítico.
- En consulta mixta, trazas de ambos especialistas.
- Registro explícito de fallos y datos no disponibles.

Documentación:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-view
