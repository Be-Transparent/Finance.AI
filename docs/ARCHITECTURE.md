# Architecture Overview

```mermaid
flowchart TD
    subgraph Frontend
        FE[Next.js UI]
    end
    subgraph Backend
        BE[FastAPI]
        DB[(PostgreSQL)]
        Cache[(Redis)]
        AI[AI/ML Service]
        Int[Integrations]
    end
    FE -->|API Calls| BE
    BE --> DB
    BE --> Cache
    BE --> AI
    BE --> Int
    Int -->|Bank APIs| Bank[Bank Services]
    Int -->|Diia| Diia[Diia Service]
    Int -->|iQ| iQ[iQ BFF]
    AI -->|Model Storage| ModelStore[(S3 / MinIO)]
```

The diagram shows the high‑level components and their interactions. The frontend talks to the FastAPI backend, which accesses the database, cache, AI/ML layer and external integrations. All services are containerised and orchestrated with Kubernetes.
