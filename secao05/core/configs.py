from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

# Crie a base de modelos do SQLAlchemy
DBBaseModel = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:38311529@localhost:5432/faculdade"
    
    # Adicione o DBBaseModel como um ClassVar
    DBBaseModel: ClassVar = DBBaseModel
    
    class Config:
        case_sensitive = True

# Instancie o objeto settings
settings: Settings = Settings()
