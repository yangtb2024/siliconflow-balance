"""
程序配置模块
"""

from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 程序配置参数
    PORT: int = 7860

    # API相关参数 
    API_KEYS: List[str]

    class Config:
        env_file = ".env"