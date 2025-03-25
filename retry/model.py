"""
重试模型模块
"""

from model.config import MODEL_LIST

def get_model():
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
