from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    app_name: str
    app_version: str
    hf_token: str
    
    class Config:
        env_file = 'src/.env'
        
        
def get_setting():
    return settings()        