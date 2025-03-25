"""
API路由模块
"""

from fastapi import APIRouter, Depends, HTTPException, Request

from model.api import get_models_list
from config.config import Settings

# 创建API路由器
router = APIRouter()

# 鉴权
def verify_authorization(request: Request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise HTTPException(status_code=401, detail="未提供 Authorization 头")
    
    parts = auth_header.split(' ')
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        raise HTTPException(status_code=401, detail="Authorization 格式无效")
    
    key = parts[1]
    if key not in Settings().ALLOW_KEYS:
        raise HTTPException(status_code=401, detail="无效的密钥")
    
    return True

@router.get("/v1/models")
@router.get("/hf/v1/models")
async def list_models(_=Depends(verify_authorization)):
    return get_models_list()

def setup_api_routes(app):
    app.include_router(router)
