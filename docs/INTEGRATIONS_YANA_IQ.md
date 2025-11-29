# Інтеграції з Yana.Diia та iQ

## 🔗 Yana.Diia Integration

### Огляд

Finance.AI надає **REST API endpoint** для Yana.Diia, що дозволяє AI-асистенту отримувати персоналізовані фінансові дані користувача.

### Endpoint

```
GET /api/integrations/yana/{user_id}
```

### Автентифікація

**Diia-Signature** (JWT, підписаний державним сервісом).

```http
Authorization: Bearer <DIIA_JWT_TOKEN>
```

### Response Payload

```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "profile": {
    "name": "Іван Іванов",
    "type": "citizen"
  },
  "financial_snapshot": {
    "balance": 12450.75,
    "currency": "UAH",
    "last_transactions": [
      {
        "id": "tx-001",
        "amount": -250.50,
        "category": "Продукти",
        "merchant": "АТБ",
        "date": "2025-11-28T10:30:00Z"
      }
    ]
  },
  "eligible_benefits": [
    {
      "code": "SUBSIDY_2025",
      "description": "Субсидія на енергоефективність",
      "amount": 3500.00
    }
  ],
  "recommendations": [
    {
      "type": "cashback",
      "message": "Ви можете отримати 5% кешбеку в АТБ через партнерську програму"
    }
  ]
}
```

### Використання в Yana

Yana.Diia використовує цей JSON для показу:

- Поточного балансу користувача
- Останніх транзакцій
- Доступних пільг та субсидій
- Персоналізованих рекомендацій

---

## 🔐 iQ Integration (iQ-BFF)

### Огляд

Finance.AI інтегрується з **iQ BFF** для підпису документів (PDF) при подачі заявок на гранти та субсидії.

### OAuth2 Flow

1. Finance.AI отримує `access_token` від iQ
2. Користувач підписує документ через iQ-підпис
3. Finance.AI зберігає підписаний файл у S3

### Endpoints

#### 1. Отримання токену

```
POST /api/integrations/iq/auth
```

**Request:**

```json
{
  "grant_type": "client_credentials",
  "client_id": "finance_ai_client",
  "client_secret": "***"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

#### 2. Підпис документа

```
POST /api/integrations/iq/sign
```

**Request:**

```json
{
  "document_url": "https://finance-ai.s3.amazonaws.com/grants/application-123.pdf",
  "user_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

**Response:**

```json
{
  "signed_document_url": "https://finance-ai.s3.amazonaws.com/grants/application-123-signed.pdf",
  "signature_timestamp": "2025-11-28T11:45:00Z",
  "signature_valid": true
}
```

### Використання

При подачі заявки на грант:

1. Користувач заповнює форму у Finance.AI
2. Генерується PDF-документ
3. Надсилається запит до iQ для підпису
4. Підписаний документ завантажується у S3
5. Посилання відправляється до державної служби

---

## 🛡️ Безпека

| Аспект | Заходи |
|--------|--------|
| **Yana.Diia** | JWT валідація, Diia-Signature перевірка, Rate-limit 10 req/s |
| **iQ BFF** | OAuth2 client credentials, TLS 1.3, Token rotation every 1h |
| **Audit** | Всі інтеграційні запити логуються у `audit_logs` |
| **PII** | Дані маскуються перед логуванням |

---

## 📚 Додаткові ресурси

- [Diia Open Source](https://github.com/diia-open-source)
- [iQ Authentication Docs](https://github.com/Be-Transparent/iQ-auth)
- [Finance.AI API Reference](API_REFERENCE.md)
