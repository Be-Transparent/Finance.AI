from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
import structlog

log = structlog.get_logger()

app = FastAPI(
    title="Finance.AI API",
    description="AI-фінансовий сервіс для громадян та ФОП України",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint for Docker/K8s"""
    return {"status": "healthy", "version": "0.1.0"}

# Routers
from backend.app.routers import auth

app.include_router(auth.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    log.info("finance_ai_startup", env=settings.ENV)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("finance_ai_shutdown")
