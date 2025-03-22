"""
服务配置模块
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 7860
