"""
面板网页路由模块
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

panel_router = APIRouter()

@panel_router.get("/", response_class=HTMLResponse)
async def index():
    return "SiliconFlow Balance"

def register_routes(app):
    app.include_router(panel_router)
