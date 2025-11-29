# Finance.AI (Diia.Фінанси)

**Державний AI-фінансовий сервіс для громадян та ФОП України**

[![CI](https://github.com/Be-Transparent/Finance.AI/workflows/CI/badge.svg)](https://github.com/Be-Transparent/Finance.AI/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🎯 Про проєкт

Finance.AI — це AI-помічник для фінансового планування та податкового обліку, інтегрований з екосистемою Diia. Надає персоналізовані рекомендації щодо пільг, грантів, субсидій та оптимізації витрат.

## ✨ Ключові функції

- 📊 **AI-категоризація транзакцій** — автоматичний розподіл витрат
- 🧾 **OCR чеків** — розпізнавання та парсинг фінансових документів
- 💰 **Eligibility Engine** — перевірка права на пільги та субсидії
- 🤖 **Персоналізовані рекомендації** — економія, кешбек, інвестиції
- 🔗 **Інтеграції** — банки, ДПС, Diia, iQ

## 🏗️ Архітектура

```
Finance.AI/
├─ backend/     # FastAPI + PostgreSQL + Redis
├─ frontend/    # Next.js 14 + Diia Design System
├─ ai/          # AI/ML моделі (PyTorch, ONNX)
├─ infra/       # Docker, K8s, Helm
├─ data/        # Схеми БД, міграції
└─ docs/        # Документація
```

Детальна архітектура: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## 🚀 Швидкий старт

### Вимоги

- Docker 24+
- Docker Compose 2.23+
- Node.js 20+ (для локальної розробки frontend)
- Python 3.11+ (для локальної розробки backend)

### Запуск

```bash
# Клонувати репозиторій
git clone https://github.com/Be-Transparent/Finance.AI.git
cd Finance.AI

# Налаштувати змінні середовища
cp .env.example .env
# Відредагуйте .env за потреби

# Запустити Docker Compose
docker compose up -d

# Перевірити статус
docker compose ps
```

Backend доступний на `http://localhost:8000`  
API Docs: `http://localhost:8000/docs`

Frontend (dev): `http://localhost:3000`

Детальніше: [docs/QUICKSTART.md](docs/QUICKSTART.md)

## 📚 Документація

- [Архітектура](docs/ARCHITECTURE.md)
- [API Reference](docs/API_REFERENCE.md)
- [AI/ML Design](docs/AI_DESIGN.md)
- [Безпека та конфіденційність](docs/SECURITY_AND_PRIVACY.md)
- [Інтеграції з Yana.Diia та iQ](docs/INTEGRATIONS_YANA_IQ.md)
- [Roadmap](docs/ROADMAP.md)

## 🧪 Тестування

```bash
# Backend tests
pytest backend/tests --cov=backend

# Frontend tests
cd frontend
npm run test:unit
npm run test:e2e
```

## 🤝 Внесок

Ми вітаємо внески від спільноти! Будь ласка, ознайомтеся з [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Ліцензія

MIT License. Детальніше: [LICENSE](LICENSE)

## 🔗 Контакти

- **Організація:** Be Transparent
- **Команда:** Igor Omelchenko (@010io)
- **Email:** contact@be-transparent.org

---

**Створено для хакатону Diia.AI 2025**
