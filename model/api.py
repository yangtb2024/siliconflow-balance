"""
模型API接口模块
"""

from model.config import MODEL_LIST

def get_models_list():
    models_list = []
    
    for model_entry in MODEL_LIST:
        model_id = model_entry
        
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

def get_chat_completions():
    pass
