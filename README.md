# 🎄 Del low-code al pro-code: Copilot Studio + Agent Engineering

Demo técnica: **Copilot Studio → VS Code → GitHub Copilot / Claude Code → SDD + Git → evaluación → ALM**, con un segundo recorrido de **Copilot Studio MCP** y Microsoft Copilot harness.

> **Estado:** material de demostración y laboratorio **ficticio**, no un agente exportado de ningún tenant. Publicado para compartir las buenas prácticas de ingeniería; ninguna acción del repositorio toca Azure, Microsoft 365 o Copilot Studio por sí sola.

## Arquitectura

![Arquitectura general](assets/carousel/01-arquitectura.svg)

En la primera ruta usamos un **agente de Copilot Studio con Standard harness** y su extensión oficial de VS Code para editar YAML. En la segunda, un **agente independiente con Microsoft Copilot harness** y el servidor MCP oficial para inspección, gestión y evaluación según los permisos disponibles. **No confundas los dos harnesses.**

## Recorrido de la sesión (45 min)

| Minutos | Momento | Evidencia |
|---|---|---|
| 0–10 | Diseño low-code del agente ElfoDesk y problema reproducible | Conversación inicial |
| 10–20 | Clonar a VS Code; SDD + IA + Git diff | Cambio revisado en YAML real |
| 20–25 | Apply a DEV y revalidación | Antes y después |
| 25–35 | Segundo agente, MCP oficial, skills y herramientas | Discovery read-only + demo disponible |
| 35–40 | Seguridad, regresión y evaluaciones | Matriz de 18 escenarios |
| 40–45 | Quality gate, ALM, observabilidad, coste | Decisión de release |

**Apply sincroniza el borrador del agente, pero NO publica.** La publicación es una acción separada.

## Estructura

- [Guion narrado](docs/02-guion-directo.md) y [arquitectura técnica](docs/03-arquitectura.md)
- [Novedades y enlaces oficiales](docs/01-novedades-verificadas.md)
- [Preparación técnica y MCP](docs/04-preparacion-tecnica.md)
- [Contrato SDD y criterios de aceptación](docs/05-sdd-contrato.md)
- [Seguridad, observabilidad y FinOps](docs/06-alm-seguridad-costes.md)
- [Evidencias para ensayar](docs/07-evidencias-demo.md)
- [Agent Framework y Foundry (extensión opcional)](docs/08-ecosistema-extendido.md)
- [Prompts](prompts/) · [Ejemplos ficticios](samples/) · [Pruebas](tests/) · [API .NET 10 opcional](bonus-dotnet-api/)
- [Carrusel visual SVG](assets/carousel/) (editable y versionable)

## Arranque rápido (sin credenciales ni servicios cloud)

```bash
python3 tests/validar_matriz.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Este CI comprueba exclusivamente la **integridad del kit y la matriz de pruebas**, no el rendimiento de un agente desplegado. Para Copilot Studio necesitas un tenant DEV autorizado, crear los agentes y ejecutar las pruebas contra ellos.

Para MCP en VS Code, usar el ejemplo **opt-in** `.vscode/mcp.example.json`; no se activa automáticamente.

## Seguridad

No hay datos de clientes ni secretos. No se deben enviar tokens, contraseñas, conversaciones reales ni ficheros exportados del tenant a un repositorio público. Revisa el código de IA antes de aplicar cambios y los permisos del MCP antes de invocar operaciones.

## Documentación oficial

- [VS Code extension](https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-overview)
- [Sincronización](https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-synchronization)
- [Copilot Studio MCP](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp)
- [Elección de harness](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness)
- [Agent evaluation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview)

**Licencia:** pendiente de definir. Este repositorio no concede por defecto una licencia open source. Última revisión documental del kit: noviembre de 2026.

