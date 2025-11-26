from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_user: str
    database_password: str
    database_name: str

settings = Settings()