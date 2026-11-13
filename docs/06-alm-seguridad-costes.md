# Quality Engineering multiagente: seguridad, observabilidad y FinOps

## Dos dimensiones distintas
- **Respuesta final:** adecuación, corrección, fundamentación, seguridad.
- **Comportamiento interno:** qué agente fue invocado, si la delegación era necesaria, fallos de conexiones y trazabilidad.

Un score conversacional favorable **no** prueba delegación correcta. Revisar la actividad/test del orquestador y registrar evidencia de especialistas llamados.

## Quality gate de la demo
| Gate | Criterio objetivo |
|---|---|
| Delegación | Security, Knowledge o ambos según matriz |
| Seguridad | Sin secretos, sin acciones destructivas |
| Precisión | FAQ no derivada innecesariamente a seguridad |
| Calidad | Score real y fallos documentados |
| Coste | Créditos/uso registrados solo si el producto los devuelve |

Metas ≠ resultados. Guardar valores en `docs/07-evidencias-demo.md`.

## Riesgos técnicos
- Permisos de acceso a Connected agents, publicación/entorno común.
- Instrucciones maliciosas en documentos externos (*prompt injection*).
- Herramientas con capacidad de efectos secundarios no deben estar presentes en esta demo.
- Mutaciones MCP: discover → plan → aprobación → cambio → prueba.
- Fallos de agente conectado, ambigüedad y costes acumulados de orquestación/evaluación.

## ALM posterior
PR de especificación → revisión → configuración Copilot Studio → evaluación → gate → promoción autorizada. Automatizar posteriormente con herramientas del tenant; no afirmar un pipeline real donde solo hay workflow de validación local.
