"""
模型API接口模块
"""

from model.config import MODEL_CONFIG

def get_models_list():
    models_list = []
    
    # 从模型配置中提取非None的模型
    for category, models in MODEL_CONFIG.items():
        for model_id, value in models.items():
            if value is None:
                continue
            
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
