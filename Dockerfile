# Multi-stage Dockerfile for Finance.AI

# ---------- Frontend Builder ----------
FROM node:20-alpine AS frontend-builder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

# ---------- Backend Builder ----------
FROM python:3.11-slim AS backend-builder
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Final Image ----------
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Runtime dependencies
RUN apt-get update && \
    apt-get install -y libpq5 curl && \
    rm -rf /var/lib/apt/lists/*

# Copy backend runtime
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY backend/ /app/backend

# Copy built frontend
COPY --from=frontend-builder /app/.next /app/.next
COPY --from=frontend-builder /app/public /app/public

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run as non-root
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
