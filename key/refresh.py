"""
密钥初始化模块
"""

import concurrent.futures

from config.config import Settings
from key.config import PAID_KEYS, FREE_REAL_KEYS, ZERO_REAL_KEYS, FREE_KEYS, ZERO_KEYS, ERROR_KEYS
from key.config import NEW_PAID_KEYS, NEW_FREE_REAL_KEYS, NEW_ZERO_REAL_KEYS, NEW_FREE_KEYS, NEW_ZERO_KEYS, NEW_ERROR_KEYS
from key.update import update_key
from log.logger import logger

def refresh_key() -> None:
    logger.info("开始刷新密钥")

    NEW_API_KEYS = Settings().API_KEYS
    NEW_API_KEYS = set(list(NEW_API_KEYS))
    
    NEW_PAID_KEYS.clear()
    NEW_FREE_REAL_KEYS.clear()
    NEW_ZERO_REAL_KEYS.clear()
    NEW_FREE_KEYS.clear()
    NEW_ZERO_KEYS.clear()
    NEW_ERROR_KEYS.clear()

    # 多线程并发处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        list(executor.map(update_key, NEW_API_KEYS))

    PAID_KEYS.clear()
    PAID_KEYS.extend(NEW_PAID_KEYS)

    FREE_REAL_KEYS.clear()
    FREE_REAL_KEYS.extend(NEW_FREE_REAL_KEYS)
    
    ZERO_REAL_KEYS.clear()
    ZERO_REAL_KEYS.extend(NEW_ZERO_REAL_KEYS)
    
    FREE_KEYS.clear()
    FREE_KEYS.extend(NEW_FREE_KEYS)
    
    ZERO_KEYS.clear()
    ZERO_KEYS.extend(NEW_ZERO_KEYS)
    
    ERROR_KEYS.clear()
    ERROR_KEYS.extend(NEW_ERROR_KEYS)

    logger.info("密钥刷新完成")

    logger.info(f"PAID_KEYS: {len(PAID_KEYS)} keys available")
    logger.info(f"PAID_KEYS: {PAID_KEYS}")

    logger.info(f"FREE_REAL_KEYS: {len(FREE_REAL_KEYS)} keys available")
    logger.info(f"FREE_REAL_KEYS: {FREE_REAL_KEYS}")

    logger.info(f"ZERO_REAL_KEYS: {len(ZERO_REAL_KEYS)} keys available")
    logger.info(f"ZERO_REAL_KEYS: {ZERO_REAL_KEYS}")

    logger.info(f"FREE_KEYS: {len(FREE_KEYS)} keys available")
    logger.info(f"FREE_KEYS: {FREE_KEYS}")

    logger.info(f"ZERO_KEYS: {len(ZERO_KEYS)} keys available")
    logger.info(f"ZERO_KEYS: {ZERO_KEYS}")

    logger.info(f"ERROR_KEYS: {len(ERROR_KEYS)} keys available")
    logger.info(f"ERROR_KEYS: {ERROR_KEYS}")
