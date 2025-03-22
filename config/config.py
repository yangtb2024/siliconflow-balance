"""
程序配置模块
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # 程序配置参数
    PORT: int = 7860
    COLOR_LOG: bool = True
    UPDATE_TIME: int = 3600
    ALLOW_KEYS: List[str] = Field(default_factory=list)

    # 端点配置参数
    BASE_URL: str = "https://api-st.siliconflow.cn/v1"

    # 密钥配置参数 
    API_KEYS: List[str] = Field(default_factory=list)

    # 模型配置参数
    REAL_MODEL: str = "meta-llama/Llama-3.3-70B-Instruct"

    class Config:
        env_file = ".env"
