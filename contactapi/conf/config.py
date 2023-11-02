from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'postgresql+psycopg2://user:password@localhost:5432/postgres'
    postgres_user: str = 'POSTGRES_USER'
    postgres_password: str = 'POSTGRES_PASSWORD'
    postgres_host: str = 'POSTGRES_HOST'
    postgres_db: str = 'POSTGRES_DB'
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()