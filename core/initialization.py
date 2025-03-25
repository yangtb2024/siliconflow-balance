"""
程序初始化模块
"""

import sys
from fastapi import FastAPI

from config.config import Settings
from core.refresh import refresh_app
from log.logger import logger
from router.api_route import setup_api_routes
from router.route import register_routes
from core.error_handler import register_error_handlers

def initialize_app() -> FastAPI:
    if not Settings().ALLOW_KEYS:
        logger.error("缺少必需的环境变量 ALLOW_KEYS, 程序将退出")
        sys.exit(1)
    
    logger.info(f"ALLOW_KEYS 验证通过, 允许的密钥数量: {len(Settings().ALLOW_KEYS)}")
    refresh_app()
    
    api_app = FastAPI(
        title="SiliconFlow Balance API", 
        description="SiliconFlow Balance",
        version="1.0.0"
    )
    
    setup_api_routes(api_app)
    logger.info("API路由注册完成")
    
    register_routes(api_app)
    logger.info("面板路由注册完成")
    
    register_error_handlers(api_app)
    logger.info("错误处理器注册完成")
    
    return api_app
