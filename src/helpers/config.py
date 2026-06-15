from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    app_name: str
    app_version: str
    hf_token: str
    
    FILE_ALLOWED_TYPES: list
    MAX_FILE_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        env_file = 'src/.env'
        
        
def get_setting():
    return settings()        