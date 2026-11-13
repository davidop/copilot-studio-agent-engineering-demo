# Evaluación reproducible de ElfoDesk

## Qué significa una buena ejecución

Evaluar **dos dimensiones**:
1. Calidad de la respuesta, con métodos y score ofrecidos por Copilot Studio Evaluate.
2. Delegación correcta, verificada por la actividad de Preview u otras trazas autorizadas.

La segunda dimensión **no queda probada automáticamente** por el score del texto final.

## Archivos

- `delegation-matrix.csv`: 8 intenciones, rutas esperadas, criterios y grupo.
- `copilot-harness-conversations.csv`: conjunto de ejemplo de 8 conversaciones; contrastar formato con el CSV oficial descargado de Copilot Studio.
- `trace-template.csv`: tabla de evidencias para fecha, run, agentes esperados, agentes observados y resultado.
- `rubric.md`: criterios de aceptación (objetivos, nunca puntuaciones supuestas).

## Demostración de 20 minutos

Seleccionar **5 casos**: SEC-01, KNO-01, MIX-01, SAFE-01 y NEG-01. La prueba MIX-01 debe permitir comprobar si se consultaron ambos especialistas, y la negativa comprobar que el orquestador no escaló un problema del cursor como robo.

En Copilot Studio, abrir ElfoDesk Orchestrator → **Evaluate** → **New evaluation**. La experiencia está documentada en preview. Revisar los métodos y créditos disponibles antes de ejecutar.

Guardar un run previo como respaldo. Si el resultado difiere de los objetivos, explicar el fallo; **no completar manualmente los campos con un aprobado ficticio**.
