from telegram.ext import Application, CommandHandler, MessageHandler, filters
from src.config.settings import TELEGRAM_BOT_TOKEN
from src.handlers.message_handlers import MessageHandlers
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    """启动机器人"""
    # 创建消息处理器
    handlers = MessageHandlers()
    
    # 创建应用
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # 添加处理器
    application.add_handler(CommandHandler("start", handlers.handle_start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_text))
    application.add_handler(MessageHandler(filters.VOICE, handlers.handle_voice))

    # 启动机器人
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main() 