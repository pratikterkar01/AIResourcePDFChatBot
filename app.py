from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Utils.logger import get_logger
from Utils.exception  import register_exception_handlers
from controller.trialController import router as trialController

logger = get_logger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Smart Building Assistant",
        description="RAG-powered Q&A over ASHRAE and BMS documents",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],          # tighten in prod
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)
    # Register routes
    app.include_router(trialController, prefix="/api")
    logger.info("FastAPI app created successfully")
    return app

app = create_app()