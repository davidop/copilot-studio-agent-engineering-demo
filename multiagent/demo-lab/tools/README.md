# consultar-stock-elfodesk — herramienta de solo lectura simulada

**Propósito:** demostrar una llamada de herramienta real desde **Knowledge Agent** y separar conocimiento estático (normas/procedimientos) de datos operativos (inventario). **Este repositorio solo incluye el contrato y un mock local**; el workflow debe crearse y publicarse en Copilot Studio DEV.

## Contrato de la herramienta

Nombre sugerido: `consultar-stock-elfodesk`. Descripción para el agente:

> Consulta la disponibilidad **simulada** de equipos IT-LAB mediante código de artículo y sede. Usar cuando el usuario pregunte si hay dispositivos de préstamo o bases USB-C. Nunca hace pedidos, reservas ni cambios. No responder con cifras de stock sin llamar a la herramienta.

**Entradas de texto**
- `itemCode`: `LOAN-14` o `DOCK-USB-C`.
- `location`: `MAD`.

**Respuesta de ejemplo (para LOAN-14 en MAD; datos ficticios):**

```json
{
  "itemCode": "LOAN-14",
  "location": "MAD",
  "knownItem": true,
  "available": true,
  "availableUnits": 2,
  "simulated": true,
  "source": "STOCK-ELFODESK-2026",
  "asOf": "2026-11-14T09:00:00+01:00",
  "operationPerformed": "read_only_lookup"
}
```

## Proceso de creación del workflow (en DEV)

1. En **Knowledge Agent → Build → Tools**, añadir un **Workflow** o seleccionar uno ya publicado, conforme a las capacidades del nuevo harness.
2. Crear `consultar-stock-elfodesk` con el trigger **When an agent calls the flow**.
3. Añadir parámetros de entrada `itemCode` y `location`. Configurar los casos de prueba estáticos:
   - `LOAN-14` + `MAD`: 2 unidades.
   - `DOCK-USB-C` + `MAD`: 0 unidades.
   - Cualquier otra combinación: `knownItem=false`, `availableUnits=0`; no afirmes que un artículo desconocido está agotado.
4. Utilizar únicamente condiciones y respuestas deterministas o una fuente **ficticia** de datos de laboratorio. No conectar ERP, Intune, Entra ID, ServiceNow ni el inventario corporativo.
5. Terminar con **Respond to the agent**, síncrono (Asynchronous response **Off**) y publicar el workflow. Es necesario responder dentro del límite documentado por Microsoft de **100 segundos**.
6. Añadir al agente Knowledge, con nombre y descripción inequívocos. En **Preview**, preguntar por LOAN-14 y comprobar **activity trace** con parámetros y salida de la herramienta.
7. No conectar esta herramienta directamente al orquestador ni a Security Agent: el **Knowledge Agent** es responsable del dato de inventario.

## Contrato local para ensayar

```bash
python multiagent/demo-lab/tools/mock_stock.py --item-code LOAN-14 --location MAD
python multiagent/demo-lab/tools/mock_stock.py --item-code DOCK-USB-C --location MAD
```

La salida solo verifica el fixture local: no constituye prueba de invocación de un workflow cloud.

Más información: https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/flow-agent
