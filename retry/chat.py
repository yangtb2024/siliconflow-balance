"""
重试 chat 模块
"""

import json
from fastapi import HTTPException

from model.config import MODEL_LIST
from key.balance import get_key
from chat.core import chat_core
from log.logger import logger

def get_chat(request_data):
    if not request_data.get("model"):
        raise HTTPException(status_code=400, detail="模型不能为空")
    
    model_id = request_data.get("model")

    if model_id not in [entry[0] for entry in MODEL_LIST]:
        raise HTTPException(status_code=404, detail="模型不存在")

    model_type = next((entry[1] for entry in MODEL_LIST if entry[0] == model_id), None)
    model_key = next((entry[2] for entry in MODEL_LIST if entry[0] == model_id), None)

    key = get_key(model_key)

    if model_type == "chat":
        formatted_json = json.dumps(request_data, indent=4, ensure_ascii=False)
        logger.info(f"收到请求, 使用密钥 {key} 处理: {formatted_json}")

        return chat_core(key, request_data)
    
    raise HTTPException(status_code=400, detail="暂不支持该类型")
