# Guion de la demo — 45 min

## 0–10 · El agente responde, pero ¿es seguro?
Abrir **ElfoDesk Standard** creado previamente en DEV. Probar «Me han robado el portátil y sospecho que han accedido a mi cuenta». Documentar la respuesta real inicial y el fallo que queremos solucionar. No garantizar que el agente fallará: preparar un defecto reproducible honesto.

## 10–20 · Salto al pro-code
Abrir el agente clonado con la extensión oficial de Copilot Studio para VS Code. Mostrar los topics y el YAML real. Crear la rama `feat/security-triage`. Pedir a GitHub Copilot/Claude Code inspección y propuesta con el contrato SDD; **no inventar artefactos**. Modificar el tema existente, ejecutar `git diff --check`, revisar cambios y correcciones en el panel Problems.

## 20–25 · Aplicar y validar
Resolver cambios remotos con Preview/Get, ejecutar **Apply a DEV** (no Publish) y repetir casos críticos, FAQ y adversariales. Registrar evidencias del antes/después.

## 25–35 · Nuevo nivel: MCP
Abrir en otro workspace el cliente MCP oficial de Copilot Studio, con un agente **Microsoft Copilot harness independiente**. Descubrir recursos y operaciones en modo lectura; identificar el entorno DEV. Mostrar su esquema de herramientas y una evaluación/consulta de consumo *solo si están disponibles*. No modificar/publicar nada sin aprobación.

## 35–40 · Quality Engineering
Enseñar `tests/casos_v2.csv`, la cobertura de urgencias, FAQ, secretos, prompt injection y falsos positivos. Distinguir los tests offline de los ejecutados en Copilot Studio. Mostrar cómo interpretar score, regresiones y límites.

## 40–45 · Enterprise Agent Engineering
PR → revisión → evaluación → gate → promoción y publicación por entornos. Riesgos: permisos, exfiltración de secretos, prompt injection, costes, trazas e idempotencia de acciones.

**Cierre:** «Low-code para expresar el negocio; pro-code para gobernar el cambio; IA para acelerar con calidad».

## Plan B
Conservar una grabación *real* del Clone, diff, Apply y test; una captura de discovery MCP y un commit de referencia. Explicar con claridad cuándo se usa la grabación. No fingir resultados.

