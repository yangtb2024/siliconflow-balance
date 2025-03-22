"""
密钥获取信息模块
"""

import requests

from log.logger import logger
from core.constants import INFO_ENDPOINT

# 获取密钥信息
def get_info(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    for i in range(3):
        try:
            response = requests.get(INFO_ENDPOINT, headers=headers)
            logger.info(f"成功获取 {response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"第 {i + 1} / 3 次获取 {api_key} 信息失败: {e}")
