# Prerrequisitos y preparación

## Camino A: Standard harness
- Copilot Studio DEV y permiso maker.
- Crear agente **ElfoDesk Standard** con conocimiento ficticio de `samples/politica-ficticia-elfodesk.md`.
- Preparar temas de bienvenida y triage inicial; verificar un fallo reproducible.
- Instalar extensión oficial de Copilot Studio para VS Code, autenticar y **Clone Agent**.
- Guardar baseline en Git; prompt de inspección → cambio pequeño → `git diff` → validar Problems → Preview/Get → **Apply** → pruebas.
- **Apply no publica.**

## Camino B: Microsoft Copilot harness y MCP
- Crear **otro** agente de ejemplo en DEV, no convertir el Standard automáticamente.
- Instalar Node/npm y disponer de un cliente MCP compatible.
- Copiar el contenido de `.vscode/mcp.example.json` a `.vscode/mcp.json` si la política de organización permite arrancar el servidor.
- El paquete `@microsoft/copilot-studio-mcp@latest` se ejecuta con npx sobre STDIO; en entornos gobernados conviene fijar una versión auditada.
- Autorizar identidad, permisos y entorno; empezar por **discovery de lectura**.
- No inventar parámetros de operaciones. Pedir descripción de acciones y comprobarlas antes de invocarlas.

Ejemplo de primer prompt:
> «Confirma identidad y entorno DEV, enumera agentes y herramientas disponibles; no cambies, apliques, pruebes ni publiques nada».

## Go / No-Go
- [ ] Entorno DEV confirmado y datos sintéticos.
- [ ] Ningún token ni secreto subido.
- [ ] Clonación y diff reproducibles.
- [ ] Editor sin errores YAML.
- [ ] Apply y pruebas reales ensayadas.
- [ ] Conexión MCP y operaciones read-only verificadas.
- [ ] Plan B de capturas/grabación listo.

Documentación:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-synchronization
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp

