"""
重试核心模块
"""

from fastapi import HTTPException

from log.logger import logger
from config.config import Settings
from retry.model import get_model
from retry.chat import get_chat

def retry_get_model():
    last_exception = None
    for i in range(Settings().RETRY_COUNT):
        try:
            response = get_model()
            return response
        except Exception as e:
            logger.error(f"第 {i+1} / {Settings().RETRY_COUNT} 次重试失败, 错误信息: {e}")
            last_exception = e

            if i == Settings().RETRY_COUNT - 1:
                raise HTTPException(status_code=500, detail=f"重试 {Settings().RETRY_COUNT} 次后获取模型失败 - {str(last_exception)}")
            else:
                continue

def retry_get_chat(request_data):
    last_exception = None
    for i in range(Settings().RETRY_COUNT):
        try:
            response = get_chat(request_data)
            return response
        except Exception as e:
            logger.error(f"第 {i+1} / {Settings().RETRY_COUNT} 次重试失败, 错误信息: {e}")
            last_exception = e

            if i == Settings().RETRY_COUNT - 1:
                raise HTTPException(status_code=500, detail=f"重试 {Settings().RETRY_COUNT} 次后获取聊天结果失败 - {str(last_exception)}")
            else:
                continue
