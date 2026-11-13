# Spec-driven Development — ElfoDesk Multi-Agent

## Objetivo
El orquestador debe **delegar** de forma verificable al especialista adecuado, responder con seguridad y preservar el comportamiento de FAQ. Ya no basta con modificar un topic YAML del Standard harness.

## Componentes
- [Contrato de delegación](../multiagent/delegation-contract.md)
- [Instrucciones Orchestrator](../multiagent/agents/orchestrator.md)
- [Security Agent](../multiagent/agents/security.md)
- [Knowledge Agent](../multiagent/agents/knowledge.md)
- [Matriz de 8 escenarios](../multiagent/evaluation/delegation-matrix.csv)

## Requisitos
1. Robo/pérdida o compromiso de cuenta → Security Agent.
2. Horario y FAQ → Knowledge Agent.
3. Consulta mixta (robo + recuperación + horario) → ambos especialistas cuando sea necesario.
4. Ambigüedad → aclaración, sin escalado injustificado.
5. Nunca solicitar secretos ni realizar acciones reales en dispositivos/identidades.
6. Cambios autorizados, revisados y trazados; registro de evaluación con fecha.

## Criterios de aceptación propuestos (no resultados)
- Traces muestran el/los agentes esperados para casos 1, 2 y 3.
- La respuesta no solicita ni expone contraseñas, MFA o tokens.
- Sin falso positivo en «he perdido el puntero».
- El test set de Evaluate devuelve puntuaciones reales que se pueden justificar.
- Se conserva instrucción anterior para rollback si la mejora degrada resultados.

**No se asume formato YAML para Microsoft Copilot harness**; las modificaciones se realizan por las superficies oficiales disponibles, incluyendo MCP, con permiso del usuario.
