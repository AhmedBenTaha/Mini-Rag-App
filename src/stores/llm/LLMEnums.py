from enum import Enum

class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"
    
    
class OpenAIEnums(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant" 
    USER = "user"   