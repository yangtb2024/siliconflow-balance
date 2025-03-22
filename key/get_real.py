"""
密钥获取实名信息模块
"""

import requests

from log.logger import logger
from core.constants import MODEL_ENDPOINT
from config.config import Settings

# 获取密钥信息
def get_real(api_key): 
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    retry_count = 3

    for i in range(retry_count):
        try:
            response = requests.get(MODEL_ENDPOINT, headers=headers, timeout=5)
            return any(item.get("id") == Settings().REAL_MODEL for item in response.json().get("data", []))
        except requests.exceptions.RequestException as e:
            logger.error(f"第 {i + 1} / {retry_count} 次获取 {api_key} 实名信息失败: {e}")

    # 查询失败
    logger.error(f"{api_key} 信息获取失败, 已重试 {retry_count} 次")
    return False
