"""
密钥初始化模块
"""

from config.config import Settings
from key.get_info import get_info

def refresh_key() -> None:
    NEW_API_KEYS = Settings().API_KEYS
    NEW_API_KEYS = set(list(NEW_API_KEYS))

    NEW_PAID_KEYS = []
    NEW_FREE_REAL_KEYS = []
    NEW_ZERO_REAL_KEYS = []
    NEW_FREE_KEYS = []
    NEW_ZERO_KEYS = []
    ERROR_KEYS = []

    for KEY in NEW_API_KEYS:
        get_info(KEY)
        