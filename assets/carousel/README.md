# Diseño y recursos del carrusel

## Versión vigente — colores claros y motivos navideños

Archivos **10–13**: versión vigente de la demo multiagente de 20 minutos, con paleta blanco hielo / azul / cian / violeta, copos de nieve y motivos navideños. Cada lámina tiene **SVG editable** y **PNG exportado (1200×1500)**.

- `10-multiagent-arquitectura.svg`: orquestador y especialistas.
- `11-multiagent-mcp.svg`: secuencia de desarrollo, VS Code + MCP + evaluación.
- `12-multiagent-evaluacion.svg`: casos de prueba y delegación esperada.
- `13-multiagent-quality-gate.svg`: decisión de calidad.

El vector del icono de **Copilot Studio** está incluido directamente en cada SVG para que GitHub lo renderice sin depender de recursos remotos. [scripts/render_carousel.py](../../scripts/render_carousel.py) exporta las cuatro láminas a PNG mediante CairoSVG; [GitHub Actions](../../.github/workflows/render-carousel.yml) ejecuta y publica la exportación cuando se actualizan las fuentes. El archivo de icono empleado y su procedencia se documentan en [assets/brand/README.md](../brand/README.md). No modificar marcas ni simular resultados.

**Aclaración:** los PNG alojados en este repositorio son renderizaciones fieles de **estos SVG claros**, no los archivos AI-render originales de la conversación. Tanto las versiones SVG como las PNG son accesibles desde el README.

Los diagramas 00–04 corresponden al diseño anterior Standard / arquitectura extendida y se conservan por compatibilidad.
