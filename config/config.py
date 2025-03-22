"""
程序配置模块
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # 程序配置参数
    PORT: int = 7860

    # 端点配置参数
    BASE_URL: str = "https://api-st.siliconflow.cn/v1"

    # 密钥配置参数 
    API_KEYS: List[str] = Field(default_factory=list)

    class Config:
        env_file = ".env"
