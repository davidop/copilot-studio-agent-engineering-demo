# Diseño y recursos del carrusel

## Diagramas técnicos SVG/PNG — colores claros y motivos navideños

Archivos **10–13**: versión vigente de la demo multiagente de 20 minutos, con paleta blanco hielo / azul / cian / violeta, copos de nieve y motivos navideños. Cada lámina tiene **SVG editable** y **PNG exportado (1200×1500)**.

- `10-multiagent-arquitectura.svg`: orquestador y especialistas.
- `11-multiagent-mcp.svg`: secuencia de desarrollo, VS Code + MCP + evaluación.
- `12-multiagent-evaluacion.svg`: casos de prueba y delegación esperada.
- `13-multiagent-quality-gate.svg`: decisión de calidad.

El vector del icono de **Copilot Studio** está incluido directamente en cada SVG para que GitHub lo renderice sin depender de recursos remotos. [scripts/render_carousel.py](../../scripts/render_carousel.py) exporta las cuatro láminas a PNG mediante CairoSVG; [GitHub Actions](../../.github/workflows/render-carousel.yml) ejecuta y publica la exportación cuando se actualizan las fuentes. El archivo de icono empleado y su procedencia se documentan en [assets/brand/README.md](../brand/README.md). No modificar marcas ni simular resultados.

**Aclaración:** los PNG alojados junto a los SVG son renderizaciones fieles de esos SVG. Las ilustraciones AI-render originales están publicadas ahora en `originals/` y son las que aparecen destacadas en la portada del proyecto.

Los diagramas 00–04 corresponden al diseño anterior Standard / arquitectura extendida y se conservan por compatibilidad.

## Ilustraciones navideñas originales (preferidas para comunicar la sesión)

Las cuatro imágenes finales del carrusel, generadas para la sesión y publicadas en formato PNG, están disponibles en la carpeta [originals](originals/). **Son las ilustraciones navideñas destacadas en el README principal**, no exportaciones de SVG.

| Archivo | Contenido |
|---|---|
| [elfodesk-architecture.png](originals/elfodesk-architecture.png) | Arquitectura multiagente con ElfoDesk Orchestrator, Rudolph Security y Noël Knowledge |
| [elfodesk-demo-flow.png](originals/elfodesk-demo-flow.png) | Flujo técnico de la demo: definir, desarrollar con IA, gestionar con MCP, probar, evaluar y aplicar Quality Gate |
| [elfodesk-agent-evaluation.png](originals/elfodesk-agent-evaluation.png) | Casos de prueba para validar delegación, seguridad y calidad |
| [elfodesk-quality-gate.png](originals/elfodesk-quality-gate.png) | Validación final de respuesta, delegación, seguridad, consumo y trazabilidad |

**Uso recomendado:** JPG originales para portadas, carruseles y sesiones; SVG + PNG derivados para diagramas técnicos versionables. Las imágenes son *infografías conceptuales*; no representan pruebas ejecutadas ni métricas de un sistema real.

