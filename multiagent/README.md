# ElfoDesk Multi-Agent · Microsoft Copilot harness

**Objetivo de la demo:** construir y probar un sistema **realmente multiagente**, con **un orquestador** y **dos especialistas** conectados en Copilot Studio, desarrollarlo/asistirlo desde GitHub Copilot en VS Code mediante el **MCP oficial**, y demostrar una evaluación repetible.

> Este repositorio contiene **especificaciones e instrucciones de ejemplo**, NO agentes desplegados ni exportaciones importables del tenant. No confundir el antiguo nombre **GitHub Copilot harness** (runtime de Copilot Studio) con **GitHub Copilot** (asistente de desarrollo).

## Componentes
- [ElfoDesk Orchestrator](agents/orchestrator.md) — interpreta, delega, sintetiza y aplica límites.
- [Security Agent](agents/security.md) — incidencias de seguridad, equipos perdidos y cuentas comprometidas.
- [Knowledge Agent](agents/knowledge.md) — horarios, FAQ, catálogo IT y recuperación aprobada.
- [Contrato de delegación](delegation-contract.md) — cuándo consultar cada agente y cómo tratar resultados.
- [Prompts MCP](prompts/mcp-bootstrap.md) y [cambio guiado](prompts/change-and-evaluate.md).
- [Mini evaluación CSV compatible](evaluation/copilot-harness-conversations.csv) y [matriz de orquestación](evaluation/delegation-matrix.csv).
- [Rúbrica](evaluation/rubric.md) y [plantilla de evidencias](evaluation/trace-template.csv).

## Preparación obligatoria (fuera del directo)
1. Confirmar que el entorno **DEV** ofrece el **Microsoft Copilot harness** y evaluación, con permisos y créditos suficientes.
2. Crear los dos especialistas en Copilot Studio, con instrucciones de este repositorio y datos **ficticios**. Publicarlos en DEV y marcarlos como **disponibles para conectarse**.
3. Crear el orquestador también con Microsoft Copilot harness. En **Build → Connected agents**, conectar especialistas publicados del **mismo entorno**, con permisos de uso apropiados.
4. Probar individualmente especialistas y después el orquestador; inspeccionar el registro/actividad del test para **verificar delegación real**, nunca inferirla solo de una respuesta convincente.
5. Configurar el [MCP oficial](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp) en VS Code, autenticar y seleccionar DEV. Confirmar `get_copilot_studio_skills`, `discover_resources` y `manage_agents` disponibles.
6. Importar el CSV de evaluación **nuevo harness** cuyo encabezado es `conversationNumber,question,response` (revisar la plantilla actual de la UI). Crear test set y ejecutar ensayo previo.
7. Guardar capturas y resultados verdaderos antes de la charla. En el directo no crear, conectar ni publicar los 3 agentes desde cero.

## Restricciones
- No contiene instrucciones para bloqueo real de cuentas, borrado remoto, envío de correos reales o uso de secretos.
- **MCP oficial de gestión** no significa que el agente consuma un servidor MCP como herramienta: son interfaces diferentes.
- El servidor MCP solo puede ejecutar operaciones anunciadas en ese tenant; **descubrir antes de actuar**, confirmar objetivo y solicitar aprobación antes de mutar.
- La evaluación es una **production-ready preview** y consume créditos según configuración. El score de respuesta no demuestra por sí mismo delegación: examinar además trazas del test y registrar el resultado por escenario.
- La prueba mixta debe hacer intervenir a **ambos especialistas si aporta valor**, sin inventar que todos los turnos requerirán paralelismo.

Fuentes:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create
