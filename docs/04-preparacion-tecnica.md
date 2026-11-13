# Preparación de la demo multiagente — 20 minutos

Consultar primero [multiagent/README.md](../multiagent/README.md) y [checklist](00-checklist-20min.md).

## 1. Agentes
En Copilot Studio DEV, crear con **Microsoft Copilot harness**:
- **ElfoDesk Orchestrator** — [instrucciones](../multiagent/agents/orchestrator.md)
- **Security Agent** — [instrucciones](../multiagent/agents/security.md)
- **Knowledge Agent** — [instrucciones](../multiagent/agents/knowledge.md)

Publicar especialistas y habilitar «available to connect». Desde el principal, usar **Build → Connected agents** para añadir ambos especialistas, dentro del mismo entorno y con acceso de participantes. Comprobar comportamiento del agente completo y trazas antes de la sesión.

## 2. GitHub Copilot + MCP oficial
Usar el ejemplo `.vscode/mcp.example.json` **únicamente si está autorizado**. Node/npx y cliente compatible, login y permisos DEV ensayados. Las herramientas concretas deben descubrirse con `get_copilot_studio_skills` y `discover_resources`; no asumir parámetros.

Prompt [bootstrap MCP](../multiagent/prompts/mcp-bootstrap.md). Para un cambio controlado: [change-and-evaluate](../multiagent/prompts/change-and-evaluate.md).

El MCP que usamos es el **servidor para operaciones sobre Copilot Studio**, no necesariamente una herramienta MCP consumida por ElfoDesk.

## 3. Agent Evaluation
Nuevo harness → pestaña **Evaluate**, siempre que esté habilitada. Preparar un conjunto pequeño con [CSV de conversaciones](../multiagent/evaluation/copilot-harness-conversations.csv) y revisar el formato que proporcione la UI. No confundir con el CSV de matrices del laboratorio Standard.

**Separar dos evidencias:** score del evaluador y **actividad/traza de Connected agents**. La respuesta final no basta para verificar la delegación. Guardar datos reales en [evidencias](07-evidencias-demo.md). Probar disponibilidad, permisos, consumo y tiempos.

## 4. Go/No-Go
- [ ] Tres agentes accesibles, especialistas publicados y conectados.
- [ ] Pruebas SECURITY, KNOWLEDGE y MIXTA con trazas de invocación.
- [ ] MCP disponible en VS Code con discovery de solo lectura.
- [ ] Eval de 5 casos preparada y un run previo auténtico guardado.
- [ ] Capturas/grabación como plan B.
- [ ] Sin credenciales reales o datos de terceros.

## Arquitectura y documentación
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create
