from ..LLMInterface import LLMInterface
from ..LLMEnums import GroqEnums
import logging
from groq import Groq


class GroqProvider(LLMInterface):

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

        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)

        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id

    def process_text(self, text: str):
        return text[: self.default_input_max_characters].strip()

    def generate_text(
        self,
        prompt: str,
        chat_history: list = None,
        max_output_tokens: int = None,
        temperature: float = None,
    ):

        if chat_history is None:
            chat_history = []

        if not self.client:
            self.logger.error("Groq client was not initialized")
            return None

        if not self.generation_model_id:
            self.logger.error("Generation model for Groq was not set")
            return None

        max_output_tokens = (
            max_output_tokens
            if max_output_tokens is not None
            else self.default_generation_max_output_tokens
        )

        temperature = (
            temperature
            if temperature is not None
            else self.default_generation_temperature
        )

        chat_history.append(
            self.construct_prompt(
                prompt=prompt,
                role=GroqEnums.USER.value,
            )
        )

        response = self.client.chat.completions.create(
            model=self.generation_model_id,
            messages=chat_history,
            max_tokens=max_output_tokens,
            temperature=temperature,
        )

        if (
            response is None
            or response.choices is None
            or len(response.choices) == 0
        ):
            self.logger.error("Error while generating text with Groq")
            return None

        return response.choices[0].message.content

    def construct_prompt(self, prompt: str, role: str):
        return {
            "role": role,
            "content": self.process_text(prompt),
        }