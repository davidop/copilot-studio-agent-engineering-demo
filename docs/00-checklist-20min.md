# Checklist GO/NO-GO — demo multiagente 20 minutos

## Preparación de agentes (fuera del directo)
- [ ] Entorno DEV y Microsoft Copilot harness disponibles en el tenant.
- [ ] Agente principal **ElfoDesk Orchestrator**.
- [ ] Dos agentes especialistas: **Security Agent** y **Knowledge Agent**, ambos publicados y conectables.
- [ ] Los tres en el mismo entorno; permisos de uso de Connected agents validados.
- [ ] Instrucciones acordes con `multiagent/agents/*.md` y datos de soporte **ficticios**.
- [ ] Consultas SECURITY, KNOWLEDGE y MIXTA ensayadas y con **traza real** de agentes invocados.
- [ ] Evitar cualquier acción de bloqueo, borrado o reset real.

## MCP (fuera del directo)
- [ ] VS Code + GitHub Copilot listos; servidor MCP oficial permitido por la organización.
- [ ] Identidad DEV autenticada, discovery del orquestador y especialistas probado.
- [ ] Contratos de herramientas comprobados; ninguna operación de publicación automática.
- [ ] Si hay cambios por MCP, se puede reproducir el plan y revertirlo; aprobación explícita.

## Agent Evaluation (fuera del directo)
- [ ] Test set con 5 casos de `multiagent/evaluation/delegation-matrix.csv`.
- [ ] Evaluador de **nuevo harness** disponible y créditos suficientes.
- [ ] CSV validado con plantilla de **la UI actual**; encabezado `conversationNumber,question,response`.
- [ ] Ejecución real previa con scores y capturas guardados.
- [ ] Registro de trazas separado de scores para probar delegación.
- [ ] Coste, tiempos y método de evaluación identificados; no inventar métricas.

## Cronómetro
| Minutos | Bloque |
|---|---|
| 0–2 | Reto multiintención |
| 2–4 | Tres agentes conectados |
| 4–9 | Delegación con trazas |
| 9–12 | VS Code + GitHub Copilot + MCP |
| 12–16 | Evaluación |
| 16–19 | Quality gate |
| 19–20 | Cierre |

**Plan B:** grabación real del ensayo y captura de evaluación, claramente etiquetadas. Si no hay permisos/connected agents/evaluación, no afirmar que la demo funciona: explicar el bloqueo y demostrar solo las capacidades verificadas.
