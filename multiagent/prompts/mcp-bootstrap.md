# Prompt para GitHub Copilot desde VS Code + Copilot Studio MCP

Conecta al **servidor MCP oficial de Copilot Studio** disponible en este cliente.

**Primera fase: solo lectura**
1. Confirma la identidad conectada y selecciona únicamente entorno DEV con permiso del usuario.
2. Utiliza `get_copilot_studio_skills` para la guía pertinente; enumera herramientas y esquemas actuales.
3. Descubre ElfoDesk Orchestrator, Security Agent y Knowledge Agent, sin asumir IDs.
4. Describe el estado de publicación y las dependencias de los agentes, si se pueden consultar.
5. Descubre acciones disponibles de `manage_agents` y los contratos con `discover_resources` / `describe_actions` si están presentes.
6. Comprueba si puedes inspeccionar y ejecutar evaluaciones del orquestador, pero **no ejecutes ninguna todavía**.
7. Devuelve un plan de cambios/probar y los recursos de los que dependerá.

No realices cambios, publicaciones, conexiones, evaluaciones de pago ni borrados sin mi aprobación explícita; no pidas credenciales ni secretos por chat. No confundas una propuesta de cambio con una operación completada.
