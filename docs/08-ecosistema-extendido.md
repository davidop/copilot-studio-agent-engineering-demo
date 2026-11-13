# Extensiones opcionales: Agent Framework y Foundry

**Microsoft Agent Framework** ofrece un modelo pro-code para agentes, herramientas, workflows, sesiones y hosting. Las skills de desarrollo para .NET/Python guían al **asistente que escribe código**; no son equivalentes a skills ejecutadas por un agente de Copilot Studio.

**Microsoft Foundry** incluye servicios para el ciclo de vida de agentes y capacidades en GA o preview según la función. Integrar Foundry como demo adicional exige otro entorno, permisos y pruebas previas.

## Bonus .NET 10
La carpeta `bonus-dotnet-api` define una **API local de triage determinista**. No bloquea cuentas ni hace llamadas a servicios. Para conectarla a Copilot Studio se requiere publicarla en HTTPS con autenticación, controles y conector autorizado. **El localhost no es accesible desde Copilot Studio cloud.**

En la charla de **20 minutos**, no ejecutar este bonus: reservar el directo para **YAML + IA + Git + Apply + MCP + evaluación**. Agent Framework, Foundry y la API .NET son material de profundización posterior.

