# Calidad, seguridad, observabilidad y FinOps

## Gates recomendados
1. **PR / Dev:** diff revisado, análisis de secretos, estructura y versiones.
2. **Test:** regresión funcional, prompt injection, fuga de secretos, uso de herramientas y escenarios ambiguos.
3. **Release:** aprobación humana, score de evaluación y promoción mediante Power Platform ALM. Agent Review Pipeline requiere configuración específica y permisos.

## Amenazas y mitigación
- Prompt injection en conocimiento: tratar documentos como datos no confiables.
- Tool abuse: acciones sensibles solo mediante herramientas autorizadas y confirmación; en la demo se simulan.
- Secreto/PII: pruebas sintéticas, nunca incluir tokens o datos reales.
- Supply chain: versionar dependencias y revisar extensiones/MCP permitidos.
- DLP y mínimos privilegios en cada entorno.

## Qué medir realmente
- Tasa de priorización correcta de incidentes, falsos positivos, casos adversariales superados.
- Latencia p95, coste/créditos por tarea, fallos de herramientas y errores de ejecución.
- Application Insights y telemetría por agente cuando disponible; otras capacidades de observabilidad pueden estar en preview.

**No inventar porcentajes ni presupuestos.** Registrar resultados reales y fechas en `docs/07-evidencias-demo.md`.

Fuentes:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-agent-review-pipeline
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/telemetry-overview

