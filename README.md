![ElfoDesk — Un taller navideño de Agent Engineering](assets/brand/elfodesk-hero.png)

---

# 🎄 ElfoDesk: del low-code al pro-code a golpe de villancico

<p align="center">
  <img src="https://img.shields.io/badge/Copilot%20Studio-Agent%20Engineering-7B61FF?style=for-the-badge" alt="Copilot Studio" />
  <img src="https://img.shields.io/badge/VS%20Code-Pro--code-5C2D91?style=for-the-badge" alt="VS Code" />
  <img src="https://img.shields.io/badge/GitHub%20Copilot-AI%20Pairing-8A63D2?style=for-the-badge" alt="GitHub Copilot" />
  <img src="https://img.shields.io/badge/MCP-Connected-6CCFC0?style=for-the-badge" alt="MCP" />
  <img src="https://img.shields.io/badge/Agent%20Evaluation-Quality%20Gate-E89AC7?style=for-the-badge" alt="Agent Evaluation" />
</p>

<p align="center">
  <strong>Por David Oliva & Érika Cepeda</strong> · Christmas Power Data Platform 2026 🎄
</p>

¿Qué ocurre cuando un agente de Copilot Studio se escapa del diseñador visual y acaba en VS Code justo antes de Navidad? 🎅🏻💻

Pues que empieza la verdadera magia.

**ElfoDesk** es una demo práctica de *Agent Engineering* en la que combinamos **Microsoft Copilot Studio, GitHub Copilot, VS Code y MCP** para entender, evolucionar y evaluar un sistema multiagente sin tener que elegir entre low-code y pro-code.

Aquí no venimos a enfrentar dos mundos.

Venimos a ponerlos a trabajar juntos. ✨

🎁 **Nuestro pequeño taller de elfos incluye:**

- 🧝‍♀️ un orquestador que decide quién debe resolver cada petición
- 🔐 un agente especializado en seguridad
- 📚 un agente especializado en conocimiento
- 🤖 IA ayudándonos desde VS Code
- 🔎 trazas para comprobar qué ha ocurrido realmente
- ✅ evaluación para descubrir si nuestros agentes se han portado bien… o merecen carbón

> 💡 **La idea:** una buena respuesta no significa necesariamente una buena arquitectura.  
> Queremos saber **qué agente actuó, por qué lo hizo y si podemos demostrarlo**.

**Low-code cuando nos hace la vida más fácil. Pro-code cuando necesitamos más control. IA para ayudarnos durante el camino.**

Y algún que otro villancico, porque estamos en Navidad. 🎄✨

## 🎁 ¿Qué vamos a desenvolver?

Todo empieza con una petición aparentemente sencilla a nuestro pequeño servicio de soporte navideño.

El problema es que detrás hay **varias intenciones, varios agentes y más de una decisión que tomar**.

A partir de ahí veremos cómo:

- 🎄 **Copilot Studio** orquesta un pequeño equipo de agentes especializados
- 💻 **VS Code + GitHub Copilot** nos ayudan a entender y evolucionar lo que estamos construyendo
- 🔌 **MCP** conecta ambos mundos
- 🧪 **Agent Evaluation + trazas** nos permiten comprobar si el sistema funciona de verdad y no solo si la respuesta “parece buena”

### El viaje

**Copilot Studio → VS Code + IA → mejora → evaluación → evidencia**

Porque en Agent Engineering el objetivo no es simplemente que el agente responda.

El objetivo es **poder confiar en cómo ha llegado hasta esa respuesta**. ✨

> 🎯 **Lo diferencial:** una respuesta buena no demuestra por sí sola que la delegación sea correcta. Queremos comprobar qué agente actuó, qué decisión tomó el orquestador y qué evidencia tenemos para demostrarlo.


**Para montar la demo en un tenant independiente:** [Guía técnica de Érika — instalación, agentes, Knowledge, Skills, workflow, MCP, Evaluate y guion de 20 minutos](docs/11-demo-erika-tenant.md).

## 🧝‍♀️ Conoce al equipo de ElfoDesk

Detrás de ElfoDesk hay tres agentes con responsabilidades muy distintas. Para la demo les hemos dado un pequeño cambio de vestuario navideño, pero debajo del gorro siguen haciendo trabajo serio. 🎄

| Miembro del taller | Nombre técnico | Su misión |
|---|---|---|
| 🎅 **ElfoDesk Orchestrator** | ElfoDesk Orchestrator | Interpreta la petición, decide qué agente debe intervenir y consolida la respuesta |
| 🛡️ **Rudolph Security** | Security Agent | Atiende pérdidas, robos, seguridad de cuentas y situaciones que requieren escalado orientativo |
| 📚 **Noël Knowledge** | Knowledge Agent | Resuelve FAQ, horarios y procedimientos de recuperación y soporte |

> 💡 Los nombres navideños forman parte del storytelling de la demo. Técnicamente seguimos trabajando con tres agentes independientes sobre el **GitHub Copilot harness de Microsoft Copilot Studio**.

El **GitHub Copilot harness de Microsoft Copilot Studio** es el runtime sobre el que trabajan los agentes; **GitHub Copilot**, en cambio, nos acompaña desde VS Code como asistente de desarrollo.

**Conectividad:** publica **Rudolph Security** y **Noël Knowledge** como agentes conectables en el mismo entorno y vincúlalos después desde **ElfoDesk Orchestrator**, revisando los permisos necesarios para la demo.

## 💻 Preparación del entorno de Érika

[**Montaje completo de VS Code + GitHub Copilot + MCP en Windows (Érika)**](docs/12-erika-vscode-mcp-windows.md) — instalación, clonación del repositorio, extensiones, configuración del servidor oficial `@microsoft/copilot-studio-mcp`, login de GitHub y Microsoft, selección de DEV, pruebas de conexión y solución de problemas.

**Archivos de referencia:** [`.mcp.example.json`](.mcp.example.json) (Copilot harness) y [`.vscode/mcp.example.json`](.vscode/mcp.example.json) (configuración del editor). Son formatos distintos: seguir la guía y confirmar la conexión en el modo seleccionado.

## 🛠️ Monta tu propio taller de ElfoDesk

¿Quieres reproducir la demo? Aquí tienes el recorrido básico para dejarlo todo preparado antes de que empiece a sonar el primer villancico. 🎶

1. **Prepara tu entorno DEV** con el **GitHub Copilot harness de Microsoft Copilot Studio** y los permisos necesarios para publicar y conectar agentes.
2. Crea y publica **Security Agent** y **Knowledge Agent** utilizando las [especificaciones ficticias](multiagent/agents/) y configúralos como conectables.
3. Crea **ElfoDesk Orchestrator**, vincula ambos especialistas desde **Build → Connected agents** y revisa los permisos.
4. Prueba consultas de seguridad, conocimiento y casos mixtos para comprobar que la **delegación es observable** desde Preview.
5. Conecta **GitHub Copilot en VS Code** al **servidor MCP de Copilot Studio** y confirma el entorno y las herramientas disponibles antes de modificar nada.
6. Prepara **Agent Evaluation**, ejecuta los casos de prueba y registra por separado los resultados y las trazas.
7. Deja listas las pantallas, evidencias y plan B para ejecutar la demo sin depender de la magia navideña de última hora. 🎄

> 🧝‍♂️ **Consejo de taller:** no improvises una mutación vía MCP durante la demo sin haber validado antes permisos, herramientas y entorno.

Para los pasos detallados, prompts, controles de seguridad y resolución de problemas, consulta el [runbook operativo completo](docs/09-runbook-paso-a-paso.md).

## 🔬 Una demostración que se puede comprobar

Ya existe un **[laboratorio de conocimiento, skills y herramientas](multiagent/demo-lab/README.md)** para explicar y ensayar el recorrido técnico completo.

| Componente | Responsable | Evidencia esperada |
|---|---|---|
| [Base SEG-INC-2026](multiagent/demo-lab/knowledge/seguridad-incidentes.md) | Rudolph Security | Respuesta fundamentada en la política de seguridad |
| [Skill security-triage](multiagent/demo-lab/skills/security-triage/SKILL.md) | Rudolph Security | Procedimiento especializado de clasificación |
| [Base IT-NAV-2026](multiagent/demo-lab/knowledge/soporte-navidad.md) | Noël Knowledge | Respuesta basada en horarios y catálogo |
| [Workflow consultar-stock-elfodesk](multiagent/demo-lab/tools/README.md) | Noël Knowledge | Tool call con inventario **ficticio** |
| [Prueba MIX-TOOL](multiagent/demo-lab/evaluation/proof-matrix.csv) | ElfoDesk Orchestrator | Dos especialistas, herramienta y trazas |

**Pregunta principal:** «Me han robado el portátil y necesito uno de préstamo LOAN-14 para mañana. ¿Quedan unidades en MAD?»

El objetivo es comprobar que ElfoDesk deriva seguridad al primer agente, conocimiento e inventario al segundo, y que este último **invoca realmente** el workflow. La respuesta del inventario es sintética; **no hay consultas a sistemas corporativos ni reservas reales**.

Los archivos y pruebas en GitHub son una **preparación reproducible**, no prueba de que el tenant DEV tenga las bases, la skill y el workflow configurados. Para la prueba real hay que cargarlos y verificar las trazas desde Copilot Studio.

## ✨ La magia visual de ElfoDesk

Porque una arquitectura multiagente también puede tener espíritu navideño.

Esta galería reúne las cuatro piezas visuales principales de la demo: **arquitectura, flujo de desarrollo, evaluación y Quality Gate**.

Las cuatro forman parte de la misma familia visual de **ElfoDesk** y cuentan, de principio a fin, cómo pasa un agente de la idea a una solución evaluada y lista para decidir si continúa… o vuelve al taller. 🎄✨

| 1. Arquitectura multiagente | 2. Flujo de desarrollo y MCP |
|:---:|:---:|
| [![ElfoDesk: arquitectura multiagente con ElfoDesk Orchestrator, Rudolph Security y Noël Knowledge](assets/carousel/originals/elfodesk-architecture.png)](assets/carousel/originals/elfodesk-architecture.png) | [![ElfoDesk: flujo de desarrollo con GitHub Copilot, MCP, pruebas, evaluación y Quality Gate](assets/carousel/originals/elfodesk-demo-flow.png)](assets/carousel/originals/elfodesk-demo-flow.png) |
| **3. Agent Evaluation** | **4. Quality Gate** |
| [![ElfoDesk: Agent Evaluation con casos de prueba, delegación, seguridad y Quality Gate](assets/carousel/originals/elfodesk-agent-evaluation.png)](assets/carousel/originals/elfodesk-agent-evaluation.png) | [![ElfoDesk: Quality Gate con respuesta correcta, delegación observada, seguridad, consumo y trazabilidad](assets/carousel/originals/elfodesk-quality-gate.png)](assets/carousel/originals/elfodesk-quality-gate.png) |

Estas ilustraciones son **PNG generados específicamente para la sesión** y forman parte de la identidad visual de ElfoDesk. Representan **arquitecturas y objetivos**, no ejecuciones verificadas en un tenant ni scores reales.

Los símbolos y denominaciones de producto se utilizan como recursos visuales para explicar la demo; este proyecto no implica patrocinio ni colaboración oficial por parte de Microsoft.

### 🧩 Dos capas visuales, dos propósitos

Las ilustraciones de ElfoDesk que ves arriba están pensadas para **comunicar la historia de la demo de forma rápida y visual**.

En paralelo, mantenemos los [SVG técnicos versionados y sus PNG exportados automáticamente](assets/carousel/README.md) para documentación, mantenimiento y slides donde necesitamos una representación más precisa y editable de la arquitectura.

En resumen:

- ✨ **Ilustraciones ElfoDesk** → storytelling, README y presentación
- 🛠️ **SVG/PNG técnicos** → arquitectura, documentación y evolución del proyecto

## 🎁 ¿Qué hay dentro de la caja?

La demo no termina cuando acaba la charla. Hemos dejado todo lo necesario para abrir ElfoDesk, entender cómo funciona y reproducir el experimento por tu cuenta.

### 🧝 Los agentes

- [Especificaciones de los tres agentes](multiagent/agents/)
- [Contrato de delegación](multiagent/delegation-contract.md)

### 🔌 La conexión entre mundos

- [Preparación técnica, permisos y MCP](docs/04-preparacion-tecnica.md)
- [Prompts para trabajar con el cliente MCP](multiagent/prompts/)

### 🧪 Las pruebas

- [Ocho escenarios multiagente](multiagent/evaluation/delegation-matrix.csv)
- [Dataset para preparar Agent Evaluation](multiagent/evaluation/copilot-harness-conversations.csv)
- [Rúbrica de evaluación](multiagent/evaluation/rubric.md)

### 🎬 Para reproducir la demo

- [Runbook paso a paso](docs/09-runbook-paso-a-paso.md)
- [Guion para el ponente](docs/10-guion-del-ponente.md)
- [Evidencias de la demo](docs/07-evidencias-demo.md)

### 🧰 Y para quien quiera seguir investigando...

- [Laboratorio legado Standard harness](legacy-standard/README.md)

> ✨ **Nuestro objetivo:** que este repo no sea solo el recuerdo de una charla de 20 minutos, sino un punto de partida para seguir experimentando con Agent Engineering.

## ✅ ¿Se han portado bien los agentes?

Antes de dar por terminado el trabajo del taller, podemos comprobar que los archivos, escenarios y pruebas locales están en orden:

```bash
python3 multiagent/validate.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

> 🎄 **Importante:** esta validación comprueba **archivos y escenarios locales**, pero no invoca Copilot Studio ni demuestra que los agentes estén funcionando correctamente en un tenant real.

Las pruebas reales deben ejecutarse sobre **ElfoDesk Orchestrator** configurado en DEV. La disponibilidad de **Agent Evaluation** puede depender del tenant y requerir créditos.

Y una regla del taller que no nos saltamos ni en Navidad: **no presentamos objetivos o datos preparados como si fueran resultados reales**. 😉

## 🧪 Antes de encender las luces del árbol...

> **Estado:** este repositorio contiene el material de preparación de la demo, no un tenant desplegado.
>
> Los tres agentes y su conexión deben crearse previamente en **Copilot Studio DEV**. Los CSV incluyen escenarios **sintéticos**, no resultados medidos.
>
> La edición YAML de la extensión clásica corresponde al **Standard harness** y se mantiene únicamente como laboratorio legado; **no forma parte de la demo principal**.

## 🔐 Seguridad y límites

Sin datos reales de clientes, tokens ni credenciales.

Ningún ejemplo bloquea dispositivos, modifica cuentas, envía correos, abre tickets o publica agentes automáticamente.

Toda mutación vía MCP necesita aprobación y comprobación del contrato real de herramientas.

## 📚 Documentación oficial

- [Conectar agentes Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected)
- [MCP oficial de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp)
- [Crear evaluaciones](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/analytics-agent-evaluation-create)
- [Elegir harness](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness)

---

## 🎄 Un último detalle antes de cerrar el taller...

Este repositorio forma parte de una demo técnica creada para explorar cómo **low-code, pro-code e IA** pueden trabajar juntos en el desarrollo de agentes.

Si algo de aquí te sirve para experimentar, aprender o construir algo mejor, entonces el taller de ElfoDesk habrá cumplido su misión. ✨

**Happy Agent Engineering & Merry Christmas!** 🎁🤖

---

**Licencia:** pendiente de definir; este repositorio no concede automáticamente licencia de código abierto.
