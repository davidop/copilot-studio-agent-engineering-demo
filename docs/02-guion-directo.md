# Guion narrado — 20 minutos (incluye MCP + evaluación)

**Concepto:** un agente de Copilot Studio es software versionable, evaluable y operable; no solo prompting.

## 00:00–02:00 — El problema
Abrir ElfoDesk Standard en DEV y preguntar: «Me han robado el portátil corporativo y creo que han accedido a mi cuenta. ¿Qué hago?».
Mostrar el comportamiento **real inicial**. «En dos minutos se hace un chatbot; convertirlo en un agente fiable requiere ingeniería». Defecto intencionado y reproducible, sin fingir fallos que no existan.

## 02:00–04:00 — Low-code → pro-code
En Copilot Studio, enseñar tema e instrucciones de seguridad en 30–45 segundos.
Pasar a VS Code con el **agente ya clonado** mediante la extensión oficial. Abrir topic YAML real y el contrato SDD; explicar brevemente el mapeo. No iniciar Clone o login en directo.

## 04:00–08:00 — IA, SDD y revisión
Utilizar el prompt [02-implementar-standard](../prompts/02-implementar-standard.md) ya ensayado, sobre un cambio mínimo (enrutamiento de incidente / respuesta segura). La IA no inventa IDs ni acciones destructivas.
Mostrar `git diff --check`, `git diff` y Problems sin errores. Si la generación tarda, enseñar el commit/diff pregrabado **real** y decirlo.

## 08:00–10:00 — Apply + contraste
Con el entorno DEV y conflictos comprobados previamente: **Apply** (no Publish).
Probar en Copilot Studio **incidencia crítica** y **FAQ inocua**. Dejar el adversarial para la mini evaluación. Mostrar el antes/después sin inventar resultados.

## 10:00–13:00 — Copilot Studio MCP (no solo YAML)
Cambiar al chat de VS Code, con **MCP oficial ya configurado y autenticado**.
Prompt: «Confirma DEV, enumera mi agente ElfoDesk y las operaciones de test/evaluación disponibles; no modifiques ni publiques nada».
Mostrar discovery de herramientas, schemas y contrato de acción de `manage_agents` cuando exista. Diferenciar **MCP de administración** de **MCP como herramienta consumida por un agente**.
El MCP gestiona el ciclo de vida según herramientas/permisos. No cambiar de harness para esta demo.

## 13:00–17:00 — Evaluar de verdad
Mini suite **3–5 casos**, creada y ensayada de antemano. Invocar evaluación por MCP **solo si el tenant expone la operación**, con confirmación de consumo/autorización. Si no, usar **Evaluación en Copilot Studio para Standard harness**, disponible separadamente y ya preparada.
Mostrar resultados reales: caso aprobado/fallido, razón y comparación si existe. *No* usar la validación de CSV local como si fuese evaluación de conversaciones.

## 17:00–19:00 — Quality gate
Pantalla con el resultado de la mini evaluación y una observación de ingeniería: seguridad, falsos positivos, costes/créditos (si se han obtenido). Decir «Sin evaluación no hay criterio objetivo de release».
Mencionar que hay **18 casos completos** en el repo y que una suite extensa/CI queda como siguiente iteración.

## 19:00–20:00 — Cierre
«Low-code para modelar el negocio. Pro-code para gobernar cambios. MCP para operar desde el IDE. Evaluación para saber si realmente mejoramos».
Mostrar QR/enlace al [repositorio](https://github.com/davidop/copilot-studio-agent-engineering-demo).

## Plan B realista
- No perder minutos en autenticación, descarga, instalaciones o generadores lentos: preparar antes.
- Captura/grabación **real**, etiquetada como ensayo previo, para Apply y evaluación si el servicio tarda o falla.
- No mezclar **Standard harness** y **Microsoft Copilot harness** como si compartieran el mismo esquema.
- No publicar ni realizar acciones reales sobre dispositivos o identidades.

Checklist: [00-checklist-20min.md](00-checklist-20min.md).
