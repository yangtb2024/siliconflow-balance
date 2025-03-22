"""
程序初始化模块
"""

from config.config import Settings
from key.config import PAID_KEYS, FREE_REAL_KEYS, FREE_KEYS, ZERO_KEYS

def initialize_app() -> None:
    NEW_API_KEYS = Settings().API_KEYS
    NEW_API_KEYS = list(set(NEW_API_KEYS))