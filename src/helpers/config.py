from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    app_name: str
    app_version: str
    hf_token: str
    
    FILE_ALLOWED_TYPES: list
    MAX_FILE_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_MAIN_DATABASE: str
    
    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str
    
    GROQ_API_KEY: str = None
    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None
    COHERE_API_KEY: str = None
    VOYAGE_API_KEY: str = None

    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DEFAULT_MAX_CHARACTERS: int = None
    GENERATION_DEFAULT_MAX_TOKENS: int = None
    GENERATION_DEFAULT_TEMPERATURE: float = None
    
    VECTOR_DB_BACKEND : str
    VECTOR_DB_PATH : str
    VECTOR_DB_DISTANCE_METHOD: str = None
    
    PRIMARY_LANG: str = None
    DEFAULT_LANG: str = None

    class Config:
        env_file = 'src/.env'
        
        
def get_setting():
    return settings()        