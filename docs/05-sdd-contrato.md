# Spec-driven Development — ElfoDesk Security Triage v2

## Problema
El agente responde FAQ, pero el enrutamiento de incidencias críticas no es suficientemente verificable ni versionado.

## Alcance
Incluye: mensajes, temas y orientaciones de seguridad **ficticias**. Excluye: bloqueo real de cuentas, borrado de dispositivos, envío de emails, tickets y publicación automática.

## Requisitos
- RF-01: Robo o pérdida de dispositivo → canal de soporte/seguridad urgente.
- RF-02: Sospecha de compromiso de credenciales → pasos seguros, nunca solicitar contraseñas, MFA, tokens ni cookies.
- RF-03: FAQ inocuas → resolución normal sin falso escalado.
- RF-04: Ambigüedad → aclarar antes de acusar una brecha.
- RF-05: Tono navideño sin trivializar incidentes.
- RNF-01: Todos los cambios en Git y entorno DEV.
- RNF-02: Validar YAML **real** con la extensión oficial; no generar IDs o referencias arbitrariamente.
- RNF-03: Ninguna operación sensible ni publicación sin autorización.

## Criterios de aceptación (metas, no resultados)
- 5/5 casos urgentes correctamente priorizados.
- 3/3 casos de secretos manejados de forma segura.
- 4/4 FAQ respondidas sin falsos positivos.
- Sin errores del esquema; diff revisado; evidencias de prueba y rollback.

## Proceso
Inspeccionar workspace real → proponer diff mínimo → revisión → validación → Apply a DEV → comprobar resultado → PR.

