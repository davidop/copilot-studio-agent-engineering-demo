# ElfoDesk · Laboratorio funcional de demostración

Este kit añade **conocimiento verificable**, una **skill real en Markdown con YAML front matter**, y un **contrato de herramienta determinista**. Permite preparar un sistema Copilot Studio que demuestre delegación, grounding, selección de skill y llamada a herramienta; **no despliega ni configura automáticamente el tenant**.

## Arquitectura y responsabilidades

| Agente | Fuente / capacidad | Objetivo |
|---|---|---|
| ElfoDesk Orchestrator | Connected agents: Security y Knowledge | Delegación y síntesis |
| Rudolph Security (Security Agent) | [Política de incidentes](knowledge/seguridad-incidentes.md) + [skill security-triage](skills/security-triage/SKILL.md) | Recomendación urgente y procedimiento de triaje |
| Noël Knowledge (Knowledge Agent) | [Manual de soporte](knowledge/soporte-navidad.md) + [workflow de consulta de stock](tools/README.md) | Horarios, procesos IT y disponibilidad **simulada** |

**No subas ambos documentos a ambos agentes ni al orquestador.** Ese aislamiento hace observable por qué necesita delegar. Cada archivo contiene referencias únicas que permiten distinguir sus respuestas.

## Instalación en Copilot Studio DEV — fuera de los 20 minutos

1. **Seguridad**: abrir **Security Agent → Build → Knowledge → Add knowledge → Upload file**. Subir solo `knowledge/seguridad-incidentes.md`. Nombrar la fuente «Política de incidentes ElfoDesk (ficticia)». En Skills, usar **Upload a skill** y cargar `skills/security-triage/SKILL.md` (contiene name y description en YAML front matter).
2. **Conocimiento**: abrir **Knowledge Agent → Build → Knowledge**, subir solo `knowledge/soporte-navidad.md`. No incluir en este documento cifras de stock; estas deben venir de una **herramienta**.
3. **Tool para Knowledge Agent**: crear un workflow `consultar-stock-elfodesk` con las entradas y salidas de [tools/README.md](tools/README.md). Este flujo es de solo lectura y responde con valores **sintéticos fijos**, nunca con inventario corporativo real. Publicar el workflow y añadirlo como herramienta al agente Knowledge.
4. **Orquestador**: conectar los dos agentes en **Build → Connected agents**; precisar sus descripciones para que Security reciba incidentes, Knowledge las FAQ y el inventario.
5. Probar individualmente cada especialista antes de ensayar con el orquestador. Confirmar en **Preview/activity trace** qué connected agents, skills y tools se activan; si el detalle de skills no está expuesto en el tenant, registrar esa limitación.
6. Crear un conjunto Evaluate con la [matriz](evaluation/proof-matrix.csv). Ejecutar las conversaciones y guardar puntuaciones **reales** y evidencias de activity trace **por separado**.
7. Ejecutar la demo preparada; para una sesión de 20 minutos, mostrar solo 3–4 preguntas y una evaluación ya configurada.

## Pregunta «wow» que prueba todo el ciclo

> «Me han robado el portátil de empresa y necesito uno de préstamo para mañana. ¿Qué hago y quedan equipos LOAN-14 en MAD?»

**Evidencia esperada, no garantizada:**
- Orchestrator delega **seguridad** a Security Agent y **disponibilidad/procedimiento** a Knowledge Agent.
- Security cita el protocolo ficticio `SEG-INC-2026` y aplica el procedimiento `security-triage`, si se muestra su activación.
- Knowledge cita el procedimiento `IT-NAV-2026` y llama al workflow `consultar-stock-elfodesk` para disponibilidad de `LOAN-14` en `MAD`.
- El workflow responde `availableUnits=2`, `simulated=true` y la fecha de fixture. El agente debe comunicar explícitamente que es un **dato simulado de laboratorio**, no inventario real.
- El resultado final prioriza el aviso de seguridad y **no** afirma haber bloqueado el dispositivo, creado un ticket o reservado equipo.
- Copilot Studio Evaluate proporciona puntuaciones de respuesta; una traza independiente confirma la delegación y tool call.

### Qué demostrar cuando algo falle

- Si Knowledge responde sobre stock sin llamar al workflow: **falla el criterio de Tool use**; no permitir que invente cantidades desde el modelo.
- Si el orquestador no delega al especialista adecuado: fallo de **routing**; revisar descripciones y contratos.
- Si un agente responde con conocimiento que solo se cargó en el otro: investigar accesos y orígenes, no dar por probada la separación.
- Si aparece una instrucción maliciosa dentro de un documento: debe tratarse como dato no confiable, no como orden.

## Verificación local — solo del material

```bash
python multiagent/demo-lab/tools/mock_stock.py --item-code LOAN-14 --location MAD
python -m unittest discover -s tests -p 'test_*.py' -v
```

El mock de Python **no está conectado automáticamente a Copilot Studio**. Para que una invocación sea realmente visible en Preview debe existir y estar conectado el workflow cloud descrito en `tools/README.md`.

## Fuentes oficiales

- [Knowledge en Microsoft Copilot harness](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-add-existing-copilot)
- [Skills de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-add-existing)
- [Workflows como herramientas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-add-workflow)
- [Conectar agentes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected)
- [Activity trace](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/preview-test-agent)
