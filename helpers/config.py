from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    app_name: str
    app_version: str
    hf_token: str
    
    FILE_ALLOWED_TYPES: list
    MAX_FILE_SIZE: int
    
    class Config:
        env_file = 'src/.env'
        
        
def get_setting():
    return settings()        