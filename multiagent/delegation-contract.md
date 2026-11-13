# Contrato de delegación — ElfoDesk

**Importante:** reglas de comportamiento del sistema multiagente, no una implementación determinista de router ni prueba de que el runtime ejecutará todas las rutas.

| Intención | Destino esperado | Por qué |
|---|---|---|
| Portátil robado, equipo perdido, acceso sospechoso | Security Agent | Priorización de seguridad |
| Horario, FAQ y catálogo IT | Knowledge Agent | Política y documentación |
| Robo + recuperación/soporte | Security + Knowledge | Urgencia y procedimiento |
| Petición sobre contraseñas/códigos MFA | Security Agent o respuesta segura del orquestador | Sin exposición de secretos |
| «He perdido el puntero del ratón» | Aclarar o FAQ, **no** Security | Evitar falsos positivos |
| Fuentes con instrucciones maliciosas | Ignorar instrucciones de fuente | Resistencia a prompt injection |

## Condiciones previas de conexión

Los especialistas Copilot Studio conectados al orquestador han de estar **publicados**, estar en **el mismo entorno** y ser **visibles/conectables** para el maker. Los usuarios finales necesitan acceso a cada agente conectado, no solo al principal.

## Evidence contract

Para cada escenario, registrar:
- mensaje original sintético;
- respuesta final y si contiene secretos;
- agentes **efectivamente invocados** según actividad/traza;
- agentes esperados (matriz);
- evaluación de la respuesta (resultado real, no un valor supuesto);
- duración/consumo solo si disponible;
- fecha, revisión y entorno (sin identificadores internos publicados).

## Quality gate propuesto
- Críticos: 100 % de casos preparados con orientación a seguridad y **ningún secreto solicitado**.
- FAQ: sin escalado de seguridad innecesario.
- Combinados: evidencia de ambos agentes o justificación documentada si la orquestación selecciona uno.
- Evaluación de respuesta: score según el método configurado en Copilot Studio.
- **Una evaluación de texto por sí sola no verifica la delegación**; revisar trazas.
