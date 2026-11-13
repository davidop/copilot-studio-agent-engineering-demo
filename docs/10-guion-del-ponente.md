# Guion para el ponente — 20 minutos

> Estas frases son propuestas para narrar la demo; las pantallas se deben ensayar. No afirmes que algo se ejecutó si solo tienes un ejemplo o una captura conceptual.

**00:00 — Apertura (20 s)**

«Hoy vamos a pasar de un agente que responde preguntas a un equipo de agentes especializados. Pero no me vale que la respuesta suene bien: quiero comprobar qué agente ha trabajado, si ha respetado las reglas y si la mejora pasa una evaluación».

**00:20–02:00 — Caso realista de demostración**

«Me han robado el portátil, creo que alguien accedió a mi cuenta y necesito saber cómo recuperar el acceso y cuándo atiende soporte». Explicar que esto mezcla **seguridad**, **procedimiento** y **horarios**.

**02:00–04:00 — Arquitectura**

«ElfoDesk no sabe hacerlo todo. Tiene un Security Agent para incidentes y un Knowledge Agent para políticas. El orquestador decide cuándo delegar, sin que el usuario tenga que escoger agente». Mostrar **Connected agents**.

**04:00–09:00 — Momento wow: delegación**

Probar en secuencia el mensaje de seguridad, el de horarios y el mixto. Señalar la evidencia real del panel Preview. «Ahora no miro solo el texto: miro quién ha intervenido. Si la consulta mixta no llamó a ambos, tenemos un problema de calidad o diseño que podemos investigar».

**09:00–12:00 — Pro-code y MCP**

«Hasta ahora he trabajado con el diseñador. Ahora paso a GitHub Copilot en VS Code y utilizo el servidor MCP oficial de Copilot Studio, con los mismos permisos del entorno». Realizar discovery de solo lectura. Mostrar el contrato de delegación y pedir una propuesta de cambio pequeña y explicada. Si se ejecuta una modificación, obtener aprobación explícita.

**12:00–16:00 — Evaluación**

«No vamos a votar si parece que responde bien. Tenemos cinco preguntas preparadas, incluidos casos ambiguos y adversariales. El evaluador nos ayuda a medir calidad, pero para saber si hubo delegación real seguimos necesitando revisar la actividad». Mostrar un run real y sus resultados, o ejecución previa fechada.

**16:00–19:00 — Quality gate**

«La respuesta correcta es necesaria, pero no suficiente». Exigir: experiencia correcta + delegación observada + seguridad + uso/consumo cuando esté disponible. Si hay fallos reales, destacarlos como hallazgos valiosos.

**19:00–20:00 — Cierre**

«Low-code nos acelera el diseño. GitHub Copilot y MCP nos acercan la ingeniería al IDE. Y la evaluación, junto con las trazas, nos permite pasar del entusiasmo a la evidencia». Mostrar enlace/QR del repositorio.

## Tres frases que evitar

- ❌ «El MCP es el protocolo que utiliza el orquestador para hablar con sus agentes». Son conceptos distintos.
- ❌ «Como responde bien, está demostrada la delegación». No sin traza.
- ❌ «La IA ha cambiado y publicado el agente». Solo si se ha autorizado y se puede demostrar la operación real.

## Pantallas y ventanas

1. Copilot Studio: **Preview y Connected agents**.
2. VS Code: **GitHub Copilot Chat con MCP oficial** y contrato de delegación abierto.
3. Copilot Studio: **Evaluate** con conjunto de prueba preparado.
4. Página de GitHub: README con galería navideña.

**No hay espacio para instalaciones, sign-in, publicación de agentes ni creación desde cero durante el directo.**
