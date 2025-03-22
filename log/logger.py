"""
日志记录模块
"""

import logging
import sys

from config.config import Settings

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: '\033[0;34m',
        logging.INFO: '\033[0;32m',
        logging.WARNING: '\033[0;33m',
        logging.ERROR: '\033[0;31m',
        logging.CRITICAL: '\033[1;41m'
    }
    RESET = '\033[0m'

    def format(self, record):
        log_message = super().format(record)
        color = self.COLORS.get(record.levelno, self.RESET)
        return f"{color}{log_message}{self.RESET}"

def get_logger(name='global_logger', log_level=logging.INFO, log_file=None):
    logger = logging.getLogger(name)
    
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    logger.setLevel(log_level)
    
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)
    
    handler = logging.FileHandler(log_file) if log_file else logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter(log_format) if Settings().COLOR_LOG else formatter)
    logger.addHandler(handler)
    
    return logger

logger = get_logger()
