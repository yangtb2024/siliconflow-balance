"""
定时任务调度模块
"""

import threading
from config.config import Settings
from core.refresh import refresh_app
from log.logger import logger

def _create_timer():
    timer = threading.Timer(Settings().UPDATE_TIME, run_refresh)
    timer.daemon = True
    return timer

def run_refresh():
    try:
        logger.info("执行定时刷新任务")
        refresh_app()
    except Exception as e:
        logger.error(f"定时刷新任务执行出错: {e}")
    finally:
        _create_timer().start()

def start_scheduler():
    timer = _create_timer()
    timer.start()
    return timer
