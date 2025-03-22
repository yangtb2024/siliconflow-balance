"""
程序刷新模块
"""

from key.refresh import refresh_key
from model.refresh import refresh_model

def refresh_app() -> None:
    refresh_key()
    refresh_model()
