# Finance.AI Roadmap

## Phase 1 – MVP (до 2025-12-15) ✅

### Backend
- [x] FastAPI server з базовою конфігурацією
- [x] PostgreSQL + Redis інтеграція
- [x] JWT автентифікація
- [ ] Core API endpoints (users, transactions, receipts)
- [ ] Alembic міграції

### Frontend
- [ ] Next.js 14 з Diia Design System
- [ ] Dashboard (огляд фінансів)
- [ ] Receipts page (завантаження чеків)
- [ ] Benefits page (перегляд пільг)

### AI
- [ ] Transaction classifier (pre-trained model)
- [ ] Basic AI service endpoint

### Infrastructure
- [x] Docker + Docker Compose
- [x] GitHub Actions CI
- [ ] Basic testing (80% coverage)

---

## Phase 2 – Integrations (до 2026-02-28)

### Integrations
- [ ] Monobank API (баланс, транзакції)
- [ ] PrivatBank API (баланс, транзакції)
- [ ] ДПС API (податкові дані)
- [ ] Diia SSO integration
- [ ] iQ BFF (підпис документів)

### AI/ML
- [ ] Receipt OCR (Tesseract + ONNX)
- [ ] Eligibility engine (перевірка пільг)
- [ ] Model retraining pipeline

### Security
- [ ] Penetration testing
- [ ] Audit log enrichment
- [ ] GDPR compliance review

### Frontend
- [ ] Grants application flow
- [ ] Integration settings page
- [ ] Real-time notifications

---

## Phase 3 – Advanced AI & Scaling (до 2026-06-30)

### AI/ML
- [ ] Recommendation engine (cashback, інвестиції)
- [ ] Advanced analytics (податкове планування)
- [ ] Airflow для model retraining

### Infrastructure
- [ ] Kubernetes deployment (production)
- [ ] Horizontal Pod Autoscaler
- [ ] Multi-region deployment (EU zone)
- [ ] Redis Cluster для масштабування

### Features
- [ ] Public API для партнерів
- [ ] Mobile app (React Native)
- [ ] Full WCAG 2.1 AA accessibility

### Observability
- [ ] Grafana dashboards
- [ ] OpenTelemetry tracing
- [ ] Advanced alerting

---

## Backlog / Future

- Multi-language support (English)
- Integration з міжнародними банками
- Blockchain-based audit trail
- Quantum-resistant encryption (Glagolitic Crypto)
