# Prompt 02 · Refactorización controlada Standard harness

Utiliza el análisis previo y `docs/05-sdd-contrato.md`.

**Objetivo:** aplicar un cambio mínimo, reversible y auditable sobre los topics reales del agente ElfoDesk Standard para:
- priorizar incidentes de robo/pérdida y posible compromiso de cuenta;
- evitar pedir contraseñas, tokens o códigos MFA;
- preservar el comportamiento de FAQ y consultas inocuas.

Reglas:
- Primero muestra los archivos y diffs propuestos.
- Pide aprobación antes de editar.
- No inventes propiedades YAML, referencias, triggers ni identificadores.
- No introduzcas acciones que afecten a dispositivos o cuentas reales.
- No ejecutes Apply, Publish ni llamadas a la nube.
- Conserva los IDs y referencias existentes salvo que tengas evidencia de que deban cambiar.

Tras la edición: explica el diff, posibles regresiones y cómo validar usando el panel Problems de VS Code y los casos de `tests/casos_v2.csv`.
