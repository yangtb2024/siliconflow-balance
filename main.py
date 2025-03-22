"""
程序入口
"""

import uvicorn

from config.config import Settings
from core.initialization import initialize_app
from log.logger import logger
from cron.scheduler import start_scheduler

# 配置
settings = Settings()

# 主程序入口
if __name__ == "__main__":
    # 初始化应用
    api_app = initialize_app()
    
    # 启动定时任务
    timer = start_scheduler()
    logger.info("定时刷新任务已启动,将在每 {} 秒执行刷新".format(settings.UPDATE_TIME))
    
    # 启动FastAPI服务
    port = settings.PORT
    logger.info("服务启动成功,监听端口: {}".format(port))
    uvicorn.run(api_app, host="0.0.0.0", port=port)
