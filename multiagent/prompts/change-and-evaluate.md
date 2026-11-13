# Prompt para evolución multiagente controlada

Contexto: demo de 20 minutos, ElfoDesk Orchestrator y dos especialistas configurados en **Microsoft Copilot harness**. Lee primero `multiagent/delegation-contract.md`, `agents/*.md` y `evaluation/delegation-matrix.csv`.

**Objetivo:** mejorar el criterio de delegación para que «Me han robado el portátil y necesito recuperar el acceso» consulte **seguridad y conocimiento**; evitar falsos positivos con «He perdido el puntero del ratón».

1. Inspecciona por MCP las definiciones **reales** del orquestador y sus conexiones; no inventes un esquema YAML para el harness nuevo.
2. Propón el cambio mínimo de instrucciones y explica riesgos, con diff de texto o configuración.
3. Pide mi aprobación antes de modificar el draft. No publiques ni conectes/distribuyas agentes nuevos por defecto.
4. Si lo apruebo, utiliza solo operaciones MCP anunciadas por el tenant y confirma el efecto real.
5. Recupera la mini evaluación preparada: usa los casos de `evaluation/copilot-harness-conversations.csv`. Comprueba el método/consumo y pide aprobación antes de ejecutarla.
6. Muestra puntuaciones obtenidas y, separadamente, **trazas de delegación reales**. Si los registros no son accesibles por MCP, usa Preview/actividad de Copilot Studio y explica el cambio de superficie.
7. Clasifica escenarios aprobados, fallidos o no verificables. No falsifiques métricas ni afirmes que se realizaron llamadas de agentes sin evidencia.

Plan de rollback: guardar la definición anterior, revertir instrucciones en DEV y repetir evaluación si se requiere.
