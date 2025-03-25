"""
API路由模块
"""

import json
from fastapi import APIRouter, Depends, HTTPException, Request

from retry.retry import retry_get_chat, retry_get_model
from config.config import Settings
from log.logger import logger

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
async def api_get_model(_=Depends(verify_authorization)):
    return retry_get_model()

@router.post("/v1/chat/completions")
@router.post("/hf/v1/chat/completions")
async def api_get_chat(request: Request, _=Depends(verify_authorization)):
    try:
        json_data = await request.json()
        return retry_get_chat(json_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="无效的 json 请求体")

def setup_api_routes(app):
    app.include_router(router)
