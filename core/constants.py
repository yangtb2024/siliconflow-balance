"""
程序常量定义模块
"""

from config.config import Settings

BASE_URL = Settings().BASE_URL

# 端点相关常量
INFO_ENDPOINT = BASE_URL + "/user/info"
MODEL_ENDPOINT = BASE_URL + "/models"
CHAT_ENDPOINT = BASE_URL + "/chat/completions"
IMAGE_ENDPOINT = BASE_URL + "/images/generations"
VOICE_ENDPOINT = BASE_URL + "/audio/speech"
EMBEDDING_ENDPOINT = BASE_URL + "/embeddings"
RERANK_ENDPOINT = BASE_URL + "/rerank"
VIDEO_ENDPOINT = BASE_URL + "/videos/submit"

# 模型相关常量
