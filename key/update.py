"""
密钥更新信息模块
"""

from log.logger import logger
from key.get_balance import get_balance
from key.get_real import get_real
from key.config import KEYS_INFO, NEW_PAID_KEYS, NEW_FREE_REAL_KEYS, NEW_ZERO_REAL_KEYS, NEW_FREE_KEYS, NEW_ZERO_KEYS, NEW_ERROR_KEYS

def update_key(api_key: str) -> None:
    balance_info = get_balance(api_key)

    if balance_info["success"] == False:
        NEW_ERROR_KEYS.append(api_key)
        return
    
    NEW_ZERO_KEYS.append(api_key)

    is_real = get_real(api_key)
    charge_balance = float(balance_info["charge_balance"])
    balance = float(balance_info["balance"])
    total_balance = float(balance_info["total_balance"])
    
    if charge_balance > 0:
        NEW_PAID_KEYS.append(api_key)
    
    if is_real and total_balance > 0:
        NEW_FREE_REAL_KEYS.append(api_key)
    
    if is_real:
        NEW_ZERO_REAL_KEYS.append(api_key)
    
    if total_balance > 0:
        NEW_FREE_KEYS.append(api_key)

    KEYS_INFO.append([api_key, balance, charge_balance, total_balance, is_real])
        
    logger.info(f"密钥 {api_key} 信息更新成功, 赠送余额: {balance}, 充值余额: {charge_balance}, 总余额: {total_balance}, 实名状态: {is_real}")
