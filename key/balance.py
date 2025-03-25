"""
密钥轮询模块
"""

from key.config import PAID_KEYS, FREE_REAL_KEYS, ZERO_REAL_KEYS, FREE_KEYS, ZERO_KEYS, ERROR_KEYS
from key.config import PAID_KEYS_POINTER, FREE_REAL_KEYS_POINTER, ZERO_REAL_KEYS_POINTER
from key.config import FREE_KEYS_POINTER, ZERO_KEYS_POINTER, ERROR_KEYS_POINTER

def get_key(key_name):
    global PAID_KEYS_POINTER, FREE_REAL_KEYS_POINTER, ZERO_REAL_KEYS_POINTER
    global FREE_KEYS_POINTER, ZERO_KEYS_POINTER, ERROR_KEYS_POINTER
    
    key = None
    
    # 根据密钥类型选择对应的密钥列表和指针
    
    if key_name == "PAID_KEYS":
        if PAID_KEYS:
            key = PAID_KEYS[PAID_KEYS_POINTER]
            PAID_KEYS_POINTER = (PAID_KEYS_POINTER + 1) % len(PAID_KEYS)
    
    elif key_name == "FREE_REAL_KEYS":
        if FREE_REAL_KEYS:
            key = FREE_REAL_KEYS[FREE_REAL_KEYS_POINTER]
            FREE_REAL_KEYS_POINTER = (FREE_REAL_KEYS_POINTER + 1) % len(FREE_REAL_KEYS)
    
    elif key_name == "ZERO_REAL_KEYS":
        if ZERO_REAL_KEYS:
            key = ZERO_REAL_KEYS[ZERO_REAL_KEYS_POINTER]
            ZERO_REAL_KEYS_POINTER = (ZERO_REAL_KEYS_POINTER + 1) % len(ZERO_REAL_KEYS)
    
    elif key_name == "FREE_KEYS":
        if FREE_KEYS:
            key = FREE_KEYS[FREE_KEYS_POINTER]
            FREE_KEYS_POINTER = (FREE_KEYS_POINTER + 1) % len(FREE_KEYS)
    
    elif key_name == "ZERO_KEYS":
        if ZERO_KEYS:
            key = ZERO_KEYS[ZERO_KEYS_POINTER]
            ZERO_KEYS_POINTER = (ZERO_KEYS_POINTER + 1) % len(ZERO_KEYS)
    
    elif key_name == "ERROR_KEYS":
        if ERROR_KEYS:
            key = ERROR_KEYS[ERROR_KEYS_POINTER]
            ERROR_KEYS_POINTER = (ERROR_KEYS_POINTER + 1) % len(ERROR_KEYS)
    
    return key
