"""
密钥获取信息模块
"""

import requests

from core.constants import INFO_ENDPOINT

# 获取密钥信息
def get_info(api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(INFO_ENDPOINT, headers=headers)
    except requests.exceptions.RequestException as e:
        pass
