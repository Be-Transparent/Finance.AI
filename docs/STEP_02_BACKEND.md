# КРОК 2: BACKEND (API) — Детальна Структура

## 📂 Структура /backend

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI application entry point
│   │
│   ├── core/                       # Core utilities
│   │   ├── __init__.py
│   │   ├── config.py               # Settings (env vars, constants)
│   │   ├── security.py             # JWT, hashing, auth utils
│   │   ├── exceptions.py           # Custom exceptions
│   │   ├── dependencies.py         # FastAPI dependencies (DB sessions)
│   │   └── logging.py              # Logging configuration
│   │
│   ├── db/                         # Database layer
│   │   ├── __init__.py
│   │   ├── base.py                 # SQLAlchemy base
│   │   ├── session.py              # DB session factory
│   │   └── repositories/           # Repository pattern (optional)
│   │       ├── __init__.py
│   │       ├── user_repo.py
│   │       ├── transaction_repo.py
│   │       └── receipt_repo.py
│   │
│   ├── models/                     # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── transaction.py
│   │   ├── receipt.py
│   │   ├── benefit.py
│   │   └── grant.py
│   │
│   ├── schemas/                    # Pydantic schemas (DTO)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── transaction.py
│   │   ├── receipt.py
│   │   ├── benefit.py
│   │   └── analytics.py
│   │
│   ├── routers/                    # API endpoints (controllers)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── transactions.py
│   │   ├── receipts.py
│   │   ├── benefits.py
│   │   ├── grants.py
│   │   ├── analytics.py
│   │   └── integrations.py
│   │
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── transaction_service.py
│   │   ├── receipt_service.py
│   │   ├── benefit_service.py
│   │   ├── grant_service.py
│   │   ├── analytics_service.py
│   │   └── ai_service.py           # Bridge to AI layer
│   │
│   └── integrations/               # External API clients
│       ├── __init__.py
│       ├── diia_client.py
│       ├── monobank_client.py
│       ├── tax_service_client.py
│       └── iq_client.py
│
├── alembic/                        # DB migrations
│   ├── versions/
│   └── env.py
│
├── tests/                          # Backend-specific tests
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── .env.example                    # Environment variables template
├── alembic.ini                     # Alembic config
├── pyproject.toml                  # Poetry/pip dependencies
└── requirements.txt                # Python dependencies
```

---

## 🔧 Основні Модулі API

### 1. **auth** — Автентифікація та авторизація

**Endpoints:**
- `POST /auth/login` — Вхід (email/password + MFA)
- `POST /auth/diia-login` — SSO через Diia
- `POST /auth/iq-login` — SSO через iQ (eID)
- `POST /auth/refresh` — Оновлення JWT токена
- `POST /auth/logout` — Вихід
- `GET /auth/me` — Дані поточного користувача

**Призначення:** Підтримка класичного OAuth, Diia SSO, iQ eID; генерація JWT токенів.

---

### 2. **users** — Управління користувачами

**Endpoints:**
- `GET /users/profile` — Профіль користувача
- `PATCH /users/profile` — Оновлення профілю
- `GET /users/settings` — Налаштування (нотифікації, мова)
- `PATCH /users/settings` — Зміна налаштувань
- `DELETE /users/account` — Видалення акаунту (GDPR)

**Призначення:** CRUD для користувачів (громадяни, ФОП), управління налаштуваннями.

---

### 3. **transactions** — Фінансові транзакції

**Endpoints:**
- `GET /transactions` — Список транзакцій (з фільтрами, пагінація)
- `POST /transactions` — Додати транзакцію (ручний ввід)
- `GET /transactions/{id}` — Деталі транзакції
- `PATCH /transactions/{id}` — Редагувати категорію/мітки
- `DELETE /transactions/{id}` — Видалити транзакцію
- `POST /transactions/import` — Імпорт з банку (CSV/Monobank API)
- `POST /transactions/classify` — AI-класифікація (batch)

**Призначення:** Облік доходів/витрат, інтеграція з банками, AI-категоризація.

---

### 4. **receipts** — Чеки та касові документи

**Endpoints:**
- `GET /receipts` — Список чеків
- `POST /receipts/upload` — Завантаження чека (QR/PDF)
- `POST /receipts/parse` — OCR + витяг даних
- `GET /receipts/{id}` — Деталі чека
- `PATCH /receipts/{id}/verify` — Підтвердження чека (manual review)
- `DELETE /receipts/{id}` — Видалити чек

**Призначення:** Управління чеками для податкової знижки, AI-парсинг (OCR).

---

### 5. **benefits** — Пільги та податкові знижки

**Endpoints:**
- `GET /benefits` — Доступні пільги (персоналізовані)
- `GET /benefits/{id}` — Деталі пільги
- `POST /benefits/check-eligibility` — Перевірка права на пільгу
- `POST /benefits/apply` — Подати заявку на пільгу
- `GET /benefits/my-applications` — Мої заявки

**Призначення:** AI-движок перевірки прав (eligibility), подача заяв.

---

### 6. **grants** — Гранти та субсидії

**Endpoints:**
- `GET /grants` — Список грантів (для ФОП)
- `GET /grants/{id}` — Деталі гранту
- `POST /grants/apply` — Подати заявку
- `GET /grants/my-applications` — Мої заявки на гранти

**Призначення:** Доступ до державних грантів для ФОП, бізнесу.

---

### 7. **analytics** — Аналітика та звіти

**Endpoints:**
- `GET /analytics/dashboard` — Фінансовий дашборд (income/expense trends)
- `GET /analytics/categories` — Розподіл витрат за категоріями
- `GET /analytics/tax-summary` — Податковий звіт (year-to-date)
- `GET /analytics/savings-report` — Рекомендації з економії
- `POST /analytics/export` — Експорт звіту (PDF/XLSX)

**Призначення:** Візуалізація фінансових даних, податкові звіти, insights.

---

### 8. **integrations** — Управління інтеграціями

**Endpoints:**
- `GET /integrations/banks` — Список підключених банків
- `POST /integrations/monobank/connect` — Підключити Monobank
- `DELETE /integrations/monobank/disconnect` — Відключити Monobank
- `POST /integrations/diia/sync` — Синхронізація даних з Diia
- `GET /integrations/yana/status` — Статус інтеграції з Yana.Diia
- `POST /integrations/iq/verify` — Верифікація через iQ (eID)

**Призначення:** Підключення зовнішніх сервісів (банки, Diia, Yana, iQ).

---

## ⚙️ Конфігурація (.env.example)

```env
# App
APP_NAME=Finance.AI
APP_ENV=development
DEBUG=True
SECRET_KEY=<generate-strong-key>

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/finance_ai

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
JWT_SECRET_KEY=<jwt-secret>
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

# External APIs
DIIA_CLIENT_ID=<diia-oauth-client-id>
DIIA_CLIENT_SECRET=<diia-oauth-secret>
MONOBANK_API_TOKEN=<monobank-token>
TAX_SERVICE_API_KEY=<tax-api-key>
IQ_API_ENDPOINT=https://iq.diia.gov.ua/api

# AI Service
AI_SERVICE_URL=http://localhost:8001
```

---

**Щоб продовжити побудову репозиторію Finance.AI — натисни далі.**
