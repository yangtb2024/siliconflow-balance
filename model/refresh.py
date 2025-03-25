"""
模型刷新模块
"""

from log.logger import logger
from model.config import MODEL_CONFIG, MODEL_LIST, NEW_MODEL_LIST

def refresh_model() -> None:
    logger.info("开始刷新模型")

    NEW_MODEL_LIST.clear()

    for model_type, models in MODEL_CONFIG.items():
        for model_name, key_type in models.items():
            if key_type is not None:
                NEW_MODEL_LIST.append([model_name, model_type, key_type])

    logger.info("模型刷新完成")

    MODEL_LIST.clear()
    MODEL_LIST.extend(NEW_MODEL_LIST)

    logger.info(f"模型列表: {MODEL_LIST}")
