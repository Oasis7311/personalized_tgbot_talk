import tempfile
import os
from gtts import gTTS
from speech_recognition import Recognizer, AudioFile
from src.config.settings import VOICE_LANG, SPEECH_RECOGNITION_LANG
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class VoiceService:
    def __init__(self):
        self.recognizer = Recognizer()
        
    async def text_to_voice(self, text: str) -> str:
        """将文本转换为语音文件"""
        try:
            tts = gTTS(text=text, lang=VOICE_LANG)
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                tts.save(temp_file.name)
                return temp_file.name
        except Exception as e:
            logger.error(f"Error converting text to voice: {e}")
            raise
            
    async def voice_to_text(self, voice_file_path: str) -> str:
        """将语音文件转换为文本"""
        try:
            with AudioFile(voice_file_path) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio, language=SPEECH_RECOGNITION_LANG)
                return text
        except Exception as e:
            logger.error(f"Error converting voice to text: {e}")
            raise
        finally:
            # 清理临时文件
            if os.path.exists(voice_file_path):
                os.unlink(voice_file_path) 