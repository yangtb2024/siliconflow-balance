"""
密钥获取信息模块
"""

import requests

from log.logger import logger
from core.constants import INFO_ENDPOINT

# 获取密钥信息
def get_balance(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    retry_count = 3

    for i in range(retry_count):
        try:
            response = requests.get(INFO_ENDPOINT, headers=headers, timeout=5)
            
            if response.status_code != 200:
                logger.error(f"获取 {api_key} 信息失败: {response.status_code} - {response.text.strip('\"')}")
                continue
                
            data = response.json().get("data")

            return {
                "success": True,
                "balance": data.get("balance"),
                "charge_balance": data.get("chargeBalance"),
                "total_balance": data.get("totalBalance")
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"第 {i + 1} / {retry_count} 次获取 {api_key} 信息失败: {e}")

    # 查询失败
    logger.error(f"{api_key} 信息获取失败，已重试 {retry_count} 次")
    return {
        "success": False,
        "balance": 0,
        "charge_balance": 0, 
        "total_balance": 0
    }
