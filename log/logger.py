"""
日志配置模块
"""

import logging
import sys

def setup_logger(name, log_level=logging.INFO, log_file=None):
    """
    设置日志记录器。

    Args:
        name (str): 日志记录器的名称。
        log_level (int): 日志级别 (logging.DEBUG, logging.INFO, etc.).
        log_file (str): 日志文件的路径。如果为 None，则输出到控制台。

    Returns:
        logging.Logger: 配置好的日志记录器。
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

# 全局日志记录器
logger = setup_logger('global_logger')
