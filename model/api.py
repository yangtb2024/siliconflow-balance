"""
模型API接口模块
"""

from fastapi import HTTPException

from model.config import MODEL_LIST
from log.logger import logger
from key.balance import get_key

def get_models_list():
    models_list = []
    
    for model_entry in MODEL_LIST:
        model_id = model_entry[0]
        
        model_info = {
            "id": model_id,
            "object": "model",
            "created": 0,
            "owned_by": ""
        }
        models_list.append(model_info)
    
    return {
        "object": "list",
        "data": models_list
    }

def get_chat_completions(request_data):
    if not request_data.get("model"):
        raise HTTPException(status_code=400, detail="模型不能为空")
    
    model_id = request_data.get("model")

    if model_id not in [entry[0] for entry in MODEL_LIST]:
        raise HTTPException(status_code=404, detail="模型不存在")

    model_type = next((entry[1] for entry in MODEL_LIST if entry[0] == model_id), None)
    model_key = next((entry[2] for entry in MODEL_LIST if entry[0] == model_id), None)

    key = get_key(model_key)

    return {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": request_data.get("model", ""),
        "usage": {
            "prompt_tokens": 13,
            "completion_tokens": 7,
            "total_tokens": 20
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "这是模型的响应"
                },
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }
