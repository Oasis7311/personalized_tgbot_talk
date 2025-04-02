import logging
from src.config.settings import LOG_FORMAT, LOG_LEVEL

def setup_logger(name):
    """设置并返回一个配置好的logger实例"""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOG_LEVEL)
    
    return logger 