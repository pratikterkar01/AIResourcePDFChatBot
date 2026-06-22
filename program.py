import uvicorn
from app import app
from Utils.Config import get_settings
from Utils.logger import get_logger

logger = get_logger(__name__)
settings = get_settings()



@app.on_event("startup")
async def on_startup():
    logger.info("Starting up ChatBot...")
    #init_chromadb()                  # initialise ChromaDB collection
   # register_all_routers(app)        # mount all controllers
    logger.info("All routers registered. App ready.")

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down gracefully...")

if __name__ == "__main__":
    uvicorn.run(
        "program:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info",
    )