# Runbook — ElfoDesk Multi-Agent: de cero a la demo de 20 minutos

**Versión:** 2026-11-13 · **Objetivo:** ejecutar una demostración verificable de delegación entre agentes en Microsoft Copilot harness, GitHub Copilot + Copilot Studio MCP y Agent Evaluation.

> **Estado de este repositorio:** especificaciones, prompts y casos ficticios listos. **No** contiene los tres agentes realmente creados en tu tenant, ni resultados de una evaluación cloud. La construcción y el ensayo del entorno DEV son pasos pendientes.

## 0. Preparar el entorno de laboratorio

**Necesitas:**
- Cuenta autorizada de Copilot Studio y entorno **DEV** separado de clientes/producción.
- Capacidad de crear agentes con el **Microsoft Copilot harness** (anteriormente GitHub Copilot harness; el texto de algunas pantallas oficiales puede conservar el nombre antiguo).
- Permisos para publicar y conectar agentes, y créditos suficientes para probarlos y evaluarlos.
- VS Code + GitHub Copilot Chat, Node.js/npm y autorización corporativa para usar el servidor MCP de Copilot Studio.
- Únicamente contenidos ficticios del repositorio; nunca credenciales, IDs privados, correos reales de clientes ni documentos de producción.

**Acciones previas:**
1. Crear o confirmar un entorno DEV.
2. Preparar la política ficticia en [samples/politica-ficticia-elfodesk.md](../samples/politica-ficticia-elfodesk.md).
3. Verificar la visibilidad de los agentes entre el maker, el usuario de evaluación y la cuenta que presente la demo.
4. Guardar capturas de la configuración **sin datos internos sensibles**.

## 1. Crear Security Agent

En Copilot Studio, crear un agente con el **nuevo harness** llamado `Security Agent`.

- Copiar/adaptar las instrucciones de [multiagent/agents/security.md](../multiagent/agents/security.md).
- Descripción recomendada: «Gestiona consultas sobre robo o pérdida de equipos corporativos, accesos no autorizados y posible compromiso de cuenta. Recomienda orientación de seguridad; **no** ejecuta bloqueos».
- No conceder acceso a sistemas reales de identidad, gestión de dispositivos ni ticketing.
- Probar individualmente: «Me han robado el portátil» → recomendaciones seguras y sin solicitud de secretos.
- Publicar y configurar la opción **Available to connect** para que se pueda seleccionar como agente conectado.

## 2. Crear Knowledge Agent

Crear un segundo agente del mismo harness llamado `Knowledge Agent`.

- Copiar/adaptar [multiagent/agents/knowledge.md](../multiagent/agents/knowledge.md).
- Añadir únicamente la política de soporte **ficticia** en la experiencia de conocimiento disponible.
- Descripción recomendada: «Responde horarios, FAQ de soporte, periféricos y procedimiento autorizado de recuperación de acceso. No clasifica ni gestiona incidentes de seguridad».
- Probar: «¿Cuál es el horario del soporte IT el 24 de diciembre?» → responder según el documento de ejemplo.
- Publicar y habilitar **Available to connect**.

## 3. Crear ElfoDesk Orchestrator

Crear `ElfoDesk Orchestrator` con Microsoft Copilot harness.

1. Copiar/adaptar las instrucciones de [multiagent/agents/orchestrator.md](../multiagent/agents/orchestrator.md).
2. En la pestaña **Build**, abrir **Connected agents** y seleccionar `Security Agent` y `Knowledge Agent`.
3. Comprobar que están **publicados y en el mismo entorno**, y que el maker es propietario o tiene el agente compartido.
4. Revisar cuidadosamente las descripciones de conexión: el motor selecciona especialistas a partir de **nombre y descripción**, petición del usuario, contexto e instrucciones del agente principal.
5. Confirmar que ambos agentes aparecen conectados.
6. Abrir **Preview** y ejecutar una pregunta de cada dominio y una consulta mixta. Comprobar la evidencia de qué especialista respondió cuando la interfaz permita mostrarlo.

> **Advertencia:** conectar dos agentes no garantiza que ambos se ejecuten para cualquier petición. La combinación puede ser secuencial o el orquestador puede omitir uno; el resultado se valida, no se presupone.

## 3A. Preparar conocimiento, skill y workflow para demostrar la arquitectura

El kit [**ElfoDesk Demo Lab**](../multiagent/demo-lab/README.md) incluye dos fuentes de conocimiento aisladas, una skill de triaje, una herramienta de consulta de inventario simulada y seis casos de verificación.

1. Abrir **Security Agent → Build → Knowledge** y subir únicamente [SEG-INC-2026](../multiagent/demo-lab/knowledge/seguridad-incidentes.md). Para esta demostración, no subir el documento general de soporte al mismo agente.
2. En **Security Agent → Build → Skills**, cargar [security-triage/SKILL.md](../multiagent/demo-lab/skills/security-triage/SKILL.md). Verificar que el harness acepta el Markdown con nombre y descripción en YAML front matter. Una skill orienta procedimientos; **no** es una llamada de servicio.
3. En **Knowledge Agent → Build → Knowledge**, subir únicamente [IT-NAV-2026](../multiagent/demo-lab/knowledge/soporte-navidad.md). Este documento contiene normas y catálogo, **sin cifras de stock**.
4. Crear el workflow [consultar-stock-elfodesk](../multiagent/demo-lab/tools/README.md): **When an agent calls the flow → condiciones deterministas → Respond to the agent**. Parámetros `itemCode` y `location`. Mantener respuesta síncrona y publicar.
5. Añadir este workflow **solo a Knowledge Agent**, comprobar nombre y descripción, y ensayar la consulta `LOAN-14` / `MAD` en Preview. La respuesta simulada del fixture son **2 unidades**; no afirmar que representan inventario real.
6. Probar el orquestador con «Me han robado el portátil y necesito uno de préstamo LOAN-14 en MAD». Registrar **los agentes realmente invocados** y la **tool call**. La respuesta textual sola no demuestra ninguno de esos pasos.
7. Comparar con la [matriz de evidencias del laboratorio](../multiagent/demo-lab/evaluation/proof-matrix.csv). Las columnas de resultados empiezan vacías y solo se completan después de ejecutar pruebas reales.

**Si Knowledge proporciona una cifra sin invocar el workflow, el test TOOL-01/MIX-TOOL debe considerarse fallido.** El archivo [mock_stock.py](../multiagent/demo-lab/tools/mock_stock.py) ofrece una simulación offline del contrato; no despliega el workflow cloud ni sustituye su traza.

## 4. Configurar GitHub Copilot + MCP oficial en VS Code

Antes del evento:
1. Instalar Node.js, disponer de `npx` y revisar la política corporativa para MCP.
2. Revisar [`.vscode/mcp.example.json`](../.vscode/mcp.example.json); copiar su servidor a `.vscode/mcp.json` **solo cuando esté autorizado**.
3. Usar el paquete oficial `@microsoft/copilot-studio-mcp` que se ejecuta por stdio. En entornos gobernados, fijar una versión validada en lugar de actualizarla automáticamente.
4. Iniciar el servidor, autenticar con la cuenta de trabajo y seleccionar **DEV**.
5. En GitHub Copilot Chat, usar [multiagent/prompts/mcp-bootstrap.md](../multiagent/prompts/mcp-bootstrap.md).
6. Mostrar herramientas disponibles, pedir guía mediante `get_copilot_studio_skills` y contrato de operaciones con `discover_resources` / `describe_actions` si la versión lo expone.
7. Inspeccionar los tres agentes y sus dependencias. **No ejecutar ninguna mutación por sorpresa**.
8. Preparar previamente una propuesta pequeña de cambio de enrutamiento a partir de [multiagent/delegation-contract.md](../multiagent/delegation-contract.md).
9. Si el tenant admite el cambio que quieres enseñar, ensayarlo en DEV con aprobación y rollback. En caso contrario, mostrar la **propuesta** y una lectura MCP real, sin fingir que la actualización ocurrió.

**Importante:** el MCP oficial usado desde VS Code sirve para **gestionar Copilot Studio**, no es el mismo mecanismo que conectar un MCP server como herramienta de un agente. La extensión clásica que edita YAML de Standard harness tampoco es la experiencia de autoría de este harness.

## 5. Preparar Agent Evaluation

En **ElfoDesk Orchestrator → Evaluate → New evaluation**:
1. Descargar de la propia UI la plantilla CSV vigente. La documentación consultada admite conjuntos de conversaciones desde CSV, creación manual y generación mediante IA.
2. Partir del archivo [multiagent/evaluation/copilot-harness-conversations.csv](../multiagent/evaluation/copilot-harness-conversations.csv) y ajustarlo a la plantilla **real**. La respuesta de referencia puede ser opcional según el método.
3. Preparar el conjunto corto recomendado: `SEC-01`, `KNO-01`, `MIX-01`, `SAFE-01`, `NEG-01`.
4. Seleccionar el método de evaluación disponible. Una calidad textual general no demuestra la delegación correcta.
5. Ejecutar un **ensayo previo real**; guardar fecha, score, fallo, método y créditos si se muestran.
6. En **Preview**, repetir las preguntas clave y registrar evidencia del especialista efectivamente invocado; completar [multiagent/evaluation/trace-template.csv](../multiagent/evaluation/trace-template.csv).
7. Tener los resultados de ese ensayo listos para mostrar como **ejecución previa**, si la evaluación tarda durante el directo.

> Esta evaluación del nuevo harness está documentada como **production-ready preview**. Crear, probar y evaluar puede consumir Copilot Credits.

## 6. Secuencia en directo (20 minutos exactos)

| Tiempo | Acción | Evidencia en pantalla |
|---|---|---|
| **0:00–2:00** | Presentar consulta mixta: robo de portátil + recuperar acceso + horario | Problema y objetivo |
| **2:00–4:00** | Mostrar ElfoDesk Orchestrator y Connected agents | 3 agentes del nuevo harness |
| **4:00–9:00** | Ejecutar **Security**, **Knowledge** y caso combinado | Respuestas y delegación observable |
| **9:00–12:00** | Cambiar a VS Code; discovery con Copilot Studio MCP | Herramientas reales; plan de mejora |
| **12:00–16:00** | Abrir Evaluate y ejecutar o revisar mini suite | Scores **reales** y casos |
| **16:00–19:00** | Contrastar evaluación y traza; comentar seguridad y consumo | Quality gate documentado |
| **19:00–20:00** | Cerrar con una idea y enlace al repositorio | «Una buena respuesta no basta» |

## 7. Plan B, por orden

- **Falla el chat multiagente:** mostrar una grabación de ensayo auténtica, claramente identificada con fecha; no recrear trazas ficticias.
- **No responde MCP:** enseñar la configuración y captura del discovery real del ensayo; no declarar una operación terminada.
- **Evaluación tarda o consume demasiado:** presentar resultados de un run real anterior, con fecha, y explicar por qué el gate no puede validarse en vivo.
- **No aparecen agentes conectados:** comprobar publicación, **Available to connect**, permisos, entorno y descripciones.
- **Un agente no se invoca:** no ocultarlo; utilizarlo como ejemplo de error de orquestación y proponer un ajuste de descripción/instrucciones.
- **Faltan créditos:** detener evaluaciones y mostrar las últimas evidencias válidas disponibles, sin generar puntuaciones simuladas.

## 8. Evidencias y criterios de éxito

La validación requiere **dos planos distintos**:

- **Experiencia:** respuesta útil, correcta, segura y sin datos confidenciales.
- **Delegación:** especialista(s) realmente consultado(s), con registro/actividad disponible.

Leer la matriz [delegation-matrix.csv](../multiagent/evaluation/delegation-matrix.csv), la [rúbrica](../multiagent/evaluation/rubric.md) y [docs/07-evidencias-demo.md](07-evidencias-demo.md). No atribuir un 100 % de éxito ni costes sin mediciones.

## Referencias oficiales

- Connected agents: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected
- MCP oficial: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp
- New harness evaluation: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create

