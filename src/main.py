from fastapi import FastAPI
from src.routes import base
from src.routes import data,nlp
from src.helpers.config import get_setting
from motor.motor_asyncio import AsyncIOMotorClient
from src.stores.llm.LLMProviderFactory import LLMProviderFactory
from src.stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from src.stores.llm.templates.template_parser import TemplateParser

app = FastAPI()


async def startup_span():
    setting = get_setting()
    app.mongo_conn = AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client = app.mongo_conn[setting.MONGODB_DATABASE]
    
    llm_provider_factory = LLMProviderFactory(setting)
    vectordb_provider_factory = VectorDBProviderFactory(setting)
    
    # generation client
    
    app.generation_client = llm_provider_factory.create(provider=setting.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id=setting.GENERATION_MODEL_ID)
    
    # Embedding Client
    app.embedding_client = llm_provider_factory.create(provider=setting.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=setting.EMBEDDING_MODEL_ID,
                                             embedding_size=setting.EMBEDDING_MODEL_SIZE)

    # vector db client
    app.vectordb_client = vectordb_provider_factory.create(provider=setting.VECTOR_DB_BACKEND)
    app.vectordb_client.connect()
    
    app.template_parser = TemplateParser(
        language=setting.PRIMARY_LANG,
        default_language=setting.DEFAULT_LANG,
    )
async def shutdown_span():
    app.mongo_conn.close()
    app.vectordb_client.disconnect()


app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)
#app.router.lifespan.on_startup.append(startup_db_client)
#app.router.lifespan.on_shutdown.append(shutdown_db_client)

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
