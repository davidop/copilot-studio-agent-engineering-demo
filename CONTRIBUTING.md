# Contribuir

Los cambios deben seguir el contrato de `docs/05-sdd-contrato.md`.

1. No incluir ningún dato real de clientes, credenciales o exports de Copilot Studio.
2. Ejecutar `python3 tests/validar_matriz.py` y `python3 -m unittest discover -s tests -p 'test_*.py' -v`.
3. Abrir PR con riesgos, diff, evidencias y procedimiento de rollback.
4. Los ejemplos de YAML son ilustrativos: la extensión oficial debe validar el esquema del agente **real clonado**.
5. Tests cloud, `Apply` y publicación solo con revisión y autorización explícita.

