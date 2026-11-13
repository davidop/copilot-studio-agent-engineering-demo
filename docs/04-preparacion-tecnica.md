# Preparación técnica · charla de 20 minutos (MCP + evaluación)

## T−1: preparar **un agente** ElfoDesk Standard

1. Usar Copilot Studio en un **entorno DEV** con permisos maker.
2. Crear ElfoDesk Standard y cargar únicamente datos ficticios de [politica-ficticia-elfodesk.md](../samples/politica-ficticia-elfodesk.md).
3. Configurar el caso inicial reproducible de *robo de portátil/compromiso de cuenta* y guardar captura de la respuesta anterior.
4. Instalar extensión oficial de Copilot Studio para VS Code y **clonar antes de la charla**.
5. Guardar el baseline del YAML real en Git y un diff de referencia sobre un topic existente; no sobrescribir con el YAML educativo de `samples/`.
6. Ensayar prompt de IA → modificación acotada → Git diff → Problems → Preview/Get → **Apply a DEV**.
7. Confirmar que el cambio se refleja en el borrador de Copilot Studio y probar **caso urgente + FAQ**.

## MCP oficial — 3 minutos

Preparar VS Code y Node/npx, identidad autenticada, permiso sobre DEV y configuración opt-in de [mcp.example.json](../.vscode/mcp.example.json). La disponibilidad del servidor está sujeta a la política y versión de tu organización.

**Prompt de demo (solo lectura):**

> «Usa exclusivamente el MCP oficial de Copilot Studio. Confirma la identidad y el entorno DEV; descubre ElfoDesk y enumera capacidades de test/evaluación realmente disponibles, sin crear, editar, aplicar ni publicar recursos».

Mostrar nombres de herramientas y esquema descubierto. No asumir argumentos ni un método de evaluación antes de inspeccionar el contrato. **MCP para gestionar Copilot Studio** no es lo mismo que MCP consumido como herramienta por un agente.

## Evaluación — 4 minutos

Preparar **una suite real de 3–5 escenarios** antes del directo. Selección de la matriz local: URG-01, FAQ-01, SEC-02, ADV-01, NEG-01. Adaptar manualmente al formato/función que ofrece el producto. Elegir método de evaluación y expectativas, comprobar permisos, tiempos y consumo.

- **Plan A:** ejecutar por MCP solo si `discover_resources`/descripción de acciones confirma una operación compatible, y tras aprobación del uso/consumo.
- **Plan B recomendado (independiente de MCP):** abrir **Evaluación en Copilot Studio para Standard harness**, con conjunto ya preparado, y ejecutar o mostrar un run anterior real, identificado como tal.
- Mostrar un aprobado/fallido y el motivo; no presentar la validación CSV de GitHub Actions como *agent evaluation*.

## Go / No-Go

- [ ] Todo en DEV con contenidos sintéticos y sin secretos.
- [ ] VS Code abierto y agente previamente clonado; no login ni instalación en directo.
- [ ] Git baseline y diff de fallback disponibles.
- [ ] Apply y dos respuestas ensayados y documentados.
- [ ] MCP autenticado, apuntando a DEV; discovery probado.
- [ ] Suite cloud ya creada y resultado de ensayo capturado.
- [ ] Se ha comprobado si existe evaluación por MCP; la UI Standard está preparada aunque no exista.
- [ ] Grabaciones reales y diferenciadas de ejecución en directo.
- [ ] Cronómetro/temporizador fuera de pantalla: máximo 20 minutos.

Recursos: [guion](02-guion-directo.md) · [checklist](00-checklist-20min.md) · [evidencias](07-evidencias-demo.md).

Documentación oficial:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-synchronization
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview
