from pydantic_settings import  BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ## server setting
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = True

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()