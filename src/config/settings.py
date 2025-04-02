import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Telegram配置
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# OpenAI配置
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = "gpt-3.5-turbo"

# 机器人配置
BOT_PERSONA = os.getenv('BOT_PERSONA', "你是一个友好的AI助手。")

# 语音配置
VOICE_LANG = 'zh-cn'
SPEECH_RECOGNITION_LANG = 'zh-CN'

# 日志配置
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO' 