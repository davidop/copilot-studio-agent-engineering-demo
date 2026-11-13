# Arquitectura de la demo

```mermaid
flowchart TB
 subgraph A["Recorrido A · Standard harness"]
   CS["Copilot Studio (DEV)"] --> VS["VS Code · Extensión oficial"]
   VS --> YAML["YAML real del agente"]
   YAML --> AI["GitHub Copilot / Claude"]
   AI --> SDD["Spec + Git diff + revisión"]
   SDD --> APPLY["Apply a DEV"]
   APPLY --> TEST["Pruebas de conversación"]
 end
 subgraph B["Recorrido B · Microsoft Copilot harness"]
   IDE["VS Code / Claude / Copilot"] --> MCP["Copilot Studio MCP oficial"]
   MCP --> DISC["Descubrir recursos y herramientas"]
   DISC --> COP["Segundo agente y skills"]
   COP --> EV["Evaluación y consumo"]
 end
 TEST --> G{"Quality gate"}
 EV --> G
 G -->|Aprobado| ALM["ALM / Publicación"]
 G -->|Rechazado| FIX["Corregir y repetir"]
```

Los recorridos usan **dos agentes distintos**; la extensión de edición YAML no garantiza equivalencia con el nuevo harness.

Diagrama SVG: [arquitectura](../assets/carousel/01-arquitectura.svg).

