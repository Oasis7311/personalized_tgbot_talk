import openai
from src.config.settings import OPENAI_API_KEY, OPENAI_MODEL, BOT_PERSONA
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class AIService:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        
    async def get_response(self, user_message: str) -> str:
        """获取AI回复"""
        try:
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": BOT_PERSONA},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error getting AI response: {e}")
            raise 