from ..LLMInterface import LLMInterface
from ..LLMEnums import DocumentTypeEnum,VoyageEnums
import voyageai
import logging


class VoyageProvider(LLMInterface):

    def __init__(
        self,
        api_key: str,
        default_input_max_characters: int = 1000,
        default_generation_max_output_tokens: int = 1000,
        default_generation_temperature: float = 0.1,
    ):

        self.api_key = api_key

        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = (
            default_generation_max_output_tokens
        )
        self.default_generation_temperature = (
            default_generation_temperature
        )

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.client = voyageai.Client(api_key=self.api_key)
        self.enums = VoyageEnums
        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size

    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()

    def generate_text(
        self,
        prompt: str,
        chat_history: list = [],
        max_output_tokens: int = None,
        temperature: float = None,
    ):
        raise NotImplementedError(
            "Voyage AI does not support text generation."
        )

    def embed_text(self, text: str, document_type: str = None):

        if not self.client:
            self.logger.error("Voyage client was not initialized")
            return None

        if not self.embedding_model_id:
            self.logger.error("Embedding model for Voyage was not set")
            return None

        input_type = DocumentTypeEnum.DOCUMENT.value

        if document_type == DocumentTypeEnum.QUERY.value:
            input_type = DocumentTypeEnum.QUERY.value

        try:
            response = self.client.embed(
                texts=[self.process_text(text)],
                model=self.embedding_model_id,
                input_type=input_type,
            )

            if (
                response is None
                or response.embeddings is None
                or len(response.embeddings) == 0
            ):
                self.logger.error("Error while embedding text with Voyage")
                return None

            return response.embeddings[0]

        except Exception as e:
            self.logger.exception(f"Voyage embedding failed: {e}")
            return None

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt),
        }