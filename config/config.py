"""
程序配置模块
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # 程序配置参数
    PORT: int = 7860

    # API相关参数 
    API_KEYS: List[str] = Field(default_factory=list)

    class Config:
        env_file = ".env"
