# Guion técnico narrado — 20 minutos multiagente

**Demo:** ElfoDesk Orchestrator + Security Agent + Knowledge Agent, todos en **Microsoft Copilot harness** y entorno DEV.

## 00:00–02:00 · El problema de un agente generalista
«Me han robado el portátil, sospecho que han accedido a mi cuenta y necesito saber cómo recupero el acceso y cuándo atiende soporte».
Mostrar la pregunta que requiere **seguridad y conocimiento**. Explicar objetivo: orquestar especialistas sin inventar acciones reales.

## 02:00–04:00 · Los tres agentes
En Copilot Studio, enseñar **ElfoDesk Orchestrator** y sus **Connected agents**: Security y Knowledge. Los especialistas ya tienen que estar creados, publicados y conectados; nada de configuración lenta en directo. Mostrar instrucciones breves y la división de responsabilidades.

## 04:00–09:00 · La delegación en acción
Ejecutar tres preguntas ensayadas:
1. Robo de portátil: esperamos Security Agent.
2. Horario de soporte: esperamos Knowledge Agent.
3. Robo + recuperación y horario: esperamos ambos especialistas.
Mostrar en el panel de actividad/diagnóstico **qué agentes se invocaron**. Una respuesta correcta sin traza no acredita multiagente. Si un agente no se invoca, mostrar la diferencia como hallazgo técnico.

## 09:00–12:00 · GitHub Copilot + VS Code + MCP
Con MCP ya autenticado en DEV, preguntar a GitHub Copilot: «inspecciona ElfoDesk y sus especialistas, enumera operaciones disponibles, no modifiques ni publiques».
Mostrar el contrato de operaciones del servidor. Pedir una **propuesta mínima** de mejora de delegación según `multiagent/delegation-contract.md`. Si la mutación está ensayada, aplicar **solo tras autorización**; si no, mostrar el diff de instrucciones previsto, sin fingir cambio remoto.

## 12:00–16:00 · Agent Evaluation
Abrir **Evaluate** del orquestador (nuevo harness), con conjunto preparado antes del directo. Mostrar los 5 casos relevantes de `multiagent/evaluation/delegation-matrix.csv`: seguridad, FAQ, mixto, secretos, ambiguo. Ejecutar la evaluación si coste y tiempo han sido ensayados; de lo contrario, mostrar una ejecución real previa **etiquetada como ensayo**.
Enseñar score/respuesta del sistema. En paralelo, comprobar delegación con trazas de Preview: la evaluación textual no prueba por sí sola las llamadas a especialistas.

## 16:00–19:00 · Quality gate
Comparar resultado real con el contrato: agente llamado, seguridad, respuesta, falsos positivos y consumo si es accesible. Mostrar 1 caso aprobado y 1 fallo si existen **realmente**. «Un agente que responde bien puede estar enrutando mal».

## 19:00–20:00 · Conclusión
«Del low-code al Agent Engineering: asistentes especializados, contratos de delegación, gestión por MCP y evaluación medible».
Mostrar QR/link a https://github.com/davidop/copilot-studio-agent-engineering-demo.

## Plan B
Autenticaciones, publicación, conexión y creación de evaluaciones están **hechas antes**. Si un servicio no responde, usar vídeo/captura **real** del ensayo, con fecha. No presentar simulaciones como ejecución en vivo. No cambiar a Standard harness ni mezclar esquemas YAML.
