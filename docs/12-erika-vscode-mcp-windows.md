# Érika — configuración de Windows/macOS, VS Code, GitHub Copilot y Copilot Studio MCP

**Objetivo:** preparar el ordenador de Érika (Windows o Mac) para desarrollar y demostrar **ElfoDesk Multi-Agent** desde **VS Code + GitHub Copilot**, con el **MCP oficial de Copilot Studio** apuntando exclusivamente a su entorno **DEV**. Este procedimiento se realiza **antes** de la sesión de 20 minutos.

> **No se ha realizado ninguna instalación ni autenticación en el equipo de Érika.** Cada comprobación marcada como «esperado» deberá verificarse allí. El acceso a un tenant y las herramientas disponibles dependen de identidad, licencia, políticas, consentimiento y entorno.

## 0. Qué hay que tener preparado

- Windows 11 o 10 actualizado y acceso a PowerShell.
- VS Code actualizado, con extensión **GitHub Copilot / GitHub Copilot Chat**, sesión GitHub autorizada y funciones de chat/agentes habilitadas.
- **Node.js LTS** compatible con el paquete publicado, `npm` y `npx` disponibles en el **mismo host** donde se ejecuta el harness.
- Git for Windows y acceso al repositorio público [copilot-studio-agent-engineering-demo](https://github.com/davidop/copilot-studio-agent-engineering-demo).
- Cuenta laboral con acceso al entorno **Copilot Studio DEV**, permisos de maker / agentes compartidos, disponibilidad de Microsoft Copilot harness y **MCP permitido por la organización**.
- Conectividad de red y permiso de ejecutar el paquete npm **`@microsoft/copilot-studio-mcp`**. Revisar la versión y su proveedor antes de autorizar ejecución.

No usar una cuenta personal de GitHub como sustituto de la identidad de trabajo que tiene permisos en Copilot Studio. Son dos inicios de sesión distintos: **GitHub Copilot** para VS Code y **Microsoft Entra** para acceder al entorno de Copilot Studio.

## 1. Instalar y comprobar las herramientas (PowerShell)

Si usa `winget`, ejecutar una vez las instalaciones necesarias (no repetir si ya están instaladas):

```powershell
winget install --id Microsoft.VisualStudioCode -e
winget install --id Git.Git -e
winget install --id OpenJS.NodeJS.LTS -e
```

Cerrar y volver a abrir VS Code / PowerShell para actualizar el PATH. Comprobar:

```powershell
code --version
git --version
node --version
npm --version
npx --version
```

**Esperado:** todos responden con una versión, sin «command not found» ni errores del PATH. Si `code` no está reconocido, abrir VS Code desde Inicio, revisar instalación/PATH y repetir en nueva terminal.

El paquete MCP se ejecutará desde el cliente con `npx`; **no** es necesario instalar `@microsoft/copilot-studio-mcp` globalmente.

## 2. Descargar el repositorio y abrirlo en VS Code

En PowerShell, elegir una carpeta local de proyectos:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\source\repos" | Out-Null
Set-Location "$HOME\source\repos"
git clone https://github.com/davidop/copilot-studio-agent-engineering-demo.git
Set-Location .\copilot-studio-agent-engineering-demo
code .
```

Si el repositorio ya existe, en su carpeta:

```powershell
git pull --ff-only
```

Abrir **Explorer** y verificar que aparecen `README.md`, `multiagent/agents/`, `multiagent/demo-lab/`, `docs/` y `.vscode/mcp.example.json`.

Recomendación: utilizar una rama propia para ensayos/documentación; **no** modificar material de demostración en `main` sin revisión.

### Alternativa macOS (sustituye las secciones 1 y 2)

En un Mac actualizado, abrir **Terminal**. Instalar Homebrew desde [brew.sh](https://brew.sh/) si aún no está disponible. Después instalar VS Code y Git:

```bash
brew install --cask visual-studio-code
brew install git
```

Instalar **Node.js LTS** desde [nodejs.org](https://nodejs.org/) (o con Homebrew si la versión ofrecida está marcada como LTS). Cerrar y volver a abrir Terminal y comprobar:

```bash
code --version
git --version
node --version
npm --version
npx --version
```

Si `code` no se reconoce, en VS Code abrir la paleta con `Cmd+Shift+P`, ejecutar **Shell Command: Install 'code' command in PATH** y abrir una Terminal nueva.

Clonar el repositorio y abrirlo:

```bash
mkdir -p "$HOME/source/repos"
cd "$HOME/source/repos"
git clone https://github.com/davidop/copilot-studio-agent-engineering-demo.git
cd copilot-studio-agent-engineering-demo
code .
```

Si ya existe el repositorio, entrar en su carpeta y ejecutar `git pull --ff-only`. En los pasos siguientes, usar `Cmd+Shift+X` en lugar de `Ctrl+Shift+X` y `Cmd+Shift+P` en lugar de `Ctrl+Shift+P`; el resto de la configuración de Copilot, MCP y Microsoft Entra es común a ambos sistemas.

## 3. Activar GitHub Copilot en VS Code

1. Abrir **Extensions** (`Ctrl+Shift+X`) e instalar/habilitar la extensión oficial **GitHub Copilot** y, cuando la versión lo requiera, **GitHub Copilot Chat** (publisher GitHub).
2. En la zona de cuentas de VS Code, seleccionar **Sign in with GitHub** y autorizar la cuenta con derecho a utilizar GitHub Copilot.
3. Abrir el panel **Chat**; comprobar que puede usar un chat de Copilot en modo agente y leer el workspace. Para la conexión MCP, seleccionar el **Copilot harness** en el selector de sesión (no el antiguo «Local»).
4. Prueba sin herramientas: «Resume las carpetas `multiagent/demo-lab` y los tres agentes ElfoDesk, sin modificar archivos». Debe devolver un resumen razonable.

Si no aparece GitHub Copilot o el modo Copilot harness, comprobar la versión de VS Code, los permisos del plan/organización y las políticas del editor. No continuar con MCP hasta resolverlo.

## 4. Conectar el MCP oficial — procedimiento recomendado (Copilot Global)

**Ésta es la opción principal para el Copilot harness nuevo.** La configuración nativa se comparte entre workspaces del mismo host, no entre equipos distintos.

1. Abrir **Chat** y seleccionar explícitamente el **Copilot harness**.
2. Abrir la paleta con `Ctrl+Shift+P`.
3. Ejecutar **Chat: Open Customizations** y entrar en **MCP Servers → Add Server**. Alternativamente usar **MCP: Add Server**.
4. Elegir un servidor **Command (stdio)**.
5. Configurar:
   - **Name / ID:** `copilotStudio`
   - **Command:** `npx`
   - **Arguments:** `-y @microsoft/copilot-studio-mcp@latest`
6. Como destino elegir **Global → Copilot Global**. No confundirlo con «VS Code User», «Local» ni `.vscode/mcp.json`.
7. Revisar el proveedor y el permiso de ejecución. Aceptar únicamente el servidor que la organización haya autorizado.
8. Guardar; desde MCP Servers comprobar que está **Enabled** y permitir que el cliente lo inicie en una sesión Copilot.

**Dónde se almacena:** habitualmente `$HOME\.copilot\mcp-config.json` (o `$COPILOT_HOME\mcp-config.json` si se definió esa variable). Lo gestiona el propio asistente de configuración. El formato nativo utiliza una raíz **`mcpServers`**, no `servers`.

**Recomendación empresarial:** sustituir `@latest` por una **versión aprobada/fijada** cuando el equipo de seguridad la haya validado. La opción `-y` solo omite la confirmación de descarga de npm; **no** concede permisos al MCP ni aprueba cambios en Copilot Studio.

### Alternativa: configuración portátil en el workspace

Para compartir el *servidor definido* en el repositorio, usar el ejemplo [`.mcp.example.json`](../.mcp.example.json) y copiarlo a `.mcp.json` **solo cuando el harness esté configurado para leerlo**. En VS Code, el destino workspace-root `.mcp.json` puede aparecer como opción experimental del asistente; un archivo existente también puede ser reconocido. Esta alternativa utiliza **`mcpServers`**.

No subir credenciales ni tokens. Cada persona debe iniciar sesión con su propia identidad y elegir su propio entorno.

### Alternativa heredada: `.vscode/mcp.json`

El archivo [`.vscode/mcp.example.json`](../.vscode/mcp.example.json) sigue en el repo por compatibilidad con el **cliente MCP administrado por el editor / antiguo Local harness**. Usa el formato raíz **`servers`**. El **Copilot harness nativo no lo lee directamente**; puede haber mecanismos de forwarding/migración, pero no deben darse por supuestos. No copiar ese archivo esperando que configure automáticamente el nuevo Copilot harness.

**Referencia:** [VS Code: MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration).

## 5. Autenticación real contra el tenant DEV

Con el MCP habilitado, abrir una conversación nueva de Copilot en VS Code y escribir:

> Conéctate al servidor MCP oficial de Copilot Studio. Enumera los entornos Microsoft disponibles para mi identidad y permite que elija uno. No crees, modifiques, publiques ni ejecutes nada.

1. Completar el inicio de sesión de **Microsoft Entra** en el navegador o ventana autorizada, incluyendo MFA si se solicita.
2. Seleccionar **exclusivamente** el entorno DEV de Érika. **No inferirlo por el nombre, no seleccionar PROD** y nunca copiar tenant IDs o tokens al repositorio.
3. Pedir: «Confirma el entorno DEV seleccionado, los agentes visibles y las herramientas que ofrece realmente el MCP; solo lectura».
4. Si están creados, comprobar que aparecen `ElfoDesk Orchestrator`, `Security Agent` y `Knowledge Agent`. Si todavía no existen, listar los recursos visibles del entorno y continuar con el montaje de Copilot Studio.
5. Revisar el **catálogo de tools**: las herramientas y esquemas efectivos se descubren en esa sesión; los ejemplos de nombres `manage_agents`, `get_copilot_studio_skills`, `discover_resources` son orientativos y pueden cambiar. No inventar argumentos ni invocar acciones destructivas.

**Criterio PASS:** se produce **al menos una llamada real de solo lectura** al servidor MCP que devuelve recursos del entorno DEV. Ver el servidor configurado o la lista de herramientas, por sí solo, no demuestra autenticación ni funcionamiento.

## 6. Comprobación de permisos y herramientas

Conserva un registro privado del ensayo:

| Comprobación | Evidencia necesaria |
|---|---|
| Copilot en VS Code | Sesión y lectura de este repositorio |
| Node/npx | Versiones sin error |
| MCP configured | `copilotStudio` enabled en Copilot Global |
| Autenticación | Inicio de sesión Entra correcto |
| Entorno | Nombre de DEV verificado |
| Discovery | Una llamada MCP real de lectura |
| Agentes | Inventario de los tres agentes cuando existan |
| Seguridad | Ninguna mutación ni publicación inesperada |

Antes de demostrar cambios por MCP, pedir **plan y diff** de instrucciones. Ejecutar una modificación en DEV solo si se han confirmado permisos, alcance y una forma de revertir. No convertir un «plan propuesto» por Copilot en «cambio aplicado».

## 7. Conectar con la demo funcional de Copilot Studio

Con MCP funcionando, preparar los recursos mediante [guía de tenant](11-demo-erika-tenant.md) y [laboratorio de pruebas](../multiagent/demo-lab/README.md):

1. **Security Agent**: instrucciones, Knowledge `SEG-INC-2026`, skill `security-triage`.
2. **Knowledge Agent**: instrucciones, Knowledge `IT-NAV-2026`, workflow publicado `consultar-stock-elfodesk`.
3. **ElfoDesk Orchestrator**: ambos especialistas conectados en el mismo entorno y permisos verificados.
4. **Preview**: ver qué especialistas se invocan; la consulta de stock debe devolver **2 unidades ficticias** exclusivamente a través de una llamada del workflow.
5. **Evaluate**: crear la suite de 5 escenarios del laboratorio, ejecutar un ensayo y conservar resultados reales, créditos si aparecen y activity traces.

El MCP utilizado aquí sirve para **trabajar con Copilot Studio desde el IDE**. No es el protocolo utilizado necesariamente entre los tres connected agents ni sustituye al workflow de Power Automate.

## 8. Guion exacto para los 3 minutos de MCP (min 10–13)

Con VS Code ya abierto y MCP autenticado:

- **10:00–10:40** — «Aquí tengo los contratos del sistema multiagente versionados en Git, no solo un diseñador visual». Abrir `multiagent/delegation-contract.md`.
- **10:40–11:40** — «Ahora GitHub Copilot utiliza MCP para consultar mi entorno DEV». Pedir el discovery **de lectura** y mostrar nombres reales de agentes; no simular llamadas.
- **11:40–12:30** — «Puedo consultar las capacidades de prueba y evaluación sin salir de VS Code». Enumerar las herramientas realmente expuestas y explicar permisos.
- **12:30–13:00** — Mostrar una propuesta de ajuste del enrutamiento, sin mutaciones si no hay ensayo/autorización. «MCP es la interfaz de ingeniería; la ejecución del agente ocurre en Copilot Studio».

El resto de la sesión sigue el [guion del ponente](10-guion-del-ponente.md).

## 9. Resolución de problemas habitual

| Síntoma | Comprobación / solución |
|---|---|
| `npx` no se reconoce | Instalar Node.js LTS, reabrir VS Code/terminal y ejecutar `npx --version` |
| El paquete no descarga | Proxy npm, política corporativa, certificado o registro; no desactivar validación TLS |
| MCP configurado, pero sin tools | Seleccionar **Copilot harness**, habilitar servidor y herramientas; revisar output del servidor y refrescar sesión |
| Copilot usa otro modo | Elegir Copilot en el selector y revisar destino: **Copilot Global** frente a Local |
| No se solicita login Entra | Pedir explícitamente el listado de entornos; revisar estado/autenticación del MCP |
| Aparece un tenant/entorno incorrecto | Detener acciones y elegir DEV; no asumir un ID a partir de documentos antiguos |
| 403 / sin permisos | Revisar maker, publicación, compartición de connected agents y consentimiento administrativo |
| El servidor se queda cargando | Revisar `node --version`, configuración, npm, logs del MCP y red |
| Funciona local pero no en SSH/Dev Container | Configurar el MCP en el **host remoto** donde se ejecuta Copilot, con Node y permisos propios |
| Configuración antigua no funciona | `.vscode/mcp.json` es formato editor `servers`; Copilot nativo requiere `mcpServers` en su destino propio |
| Evaluación no disponible | Comprobar características preview, créditos y permisos del tenant; no fabricar puntuaciones |

## 10. Criterio final GO/NO-GO

**GO del entorno VS Code + MCP** si hay acceso a la carpeta de trabajo, Copilot operativo, servidor instalado y **al menos un discovery real de recursos DEV**.  
**GO de la demo multiagente** si además están los tres agentes conectados, Knowledge + Skill + Workflow operativos, una traza mixta real y al menos una evaluación con resultados verificados.

No aceptar como prueba de un sistema desplegado la mera presencia de los archivos `.md`, `.json` o el mock Python.

## Documentación Microsoft / VS Code

- [Copilot Studio MCP — conectar VS Code y GitHub Copilot CLI](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp-vscode-copilot-cli)
- [Copilot Studio MCP — permisos](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp-configure)
- [Copilot Studio MCP — funciones](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/copilot-studio-mcp)
- [VS Code — añadir servidores](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [VS Code — esquema y destinos](https://code.visualstudio.com/docs/agents/reference/mcp-configuration)
- [VS Code — gestión y diagnóstico](https://code.visualstudio.com/docs/agents/run/manage-mcp-servers)
