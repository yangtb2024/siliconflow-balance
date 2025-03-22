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
        raise HTTPException(status_code=401, detail="未提供Authorization头")
    
    try:
        key = auth_header.split(' ')[1]
        if key not in Settings().ALLOW_KEYS:
            raise HTTPException(status_code=401, detail="无效的API密钥")
    except Exception:
        raise HTTPException(status_code=401, detail="Authorization格式无效")
    
    return True

@router.get("/v1/models")
@router.get("/hf/v1/models")
async def list_models(_=Depends(verify_authorization)):
    return get_models_list()

def setup_api_routes(app):
    app.include_router(router)
