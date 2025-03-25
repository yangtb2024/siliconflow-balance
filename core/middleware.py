"""
程序处理请求模块
"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from log.logger import logger
import time

class RealIPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # 保存原始客户端信息
        original_client = request.client
        
        # 获取真实IP
        if "X-Forwarded-For" in request.headers:
            real_ip = request.headers["X-Forwarded-For"].split(",")[0].strip()
        elif "X-Real-IP" in request.headers:
            real_ip = request.headers["X-Real-IP"]
        elif "CF-Connecting-IP" in request.headers:
            real_ip = request.headers["CF-Connecting-IP"]
        else:
            real_ip = request.client.host if request.client else None
        
        # 存储在request.state中
        request.state.real_ip = real_ip
        
        # 修改request.client对象，使FastAPI日志能正确显示真实IP
        if real_ip and original_client:
            # 创建一个新的client tuple，保留原端口但更改IP
            from starlette.datastructures import Address
            request._headers.append((b"X-Original-Client", str(original_client).encode()))
            request.scope["client"] = Address(real_ip, original_client.port)
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        
        logger.info(
            f"{real_ip}:{request.client.port} - \"{request.method} {request.url.path} "
            f"{request.scope.get('http_version', 'HTTP/1.1')}\" {response.status_code} "
            f"- 处理时间: {process_time:.4f}秒"
        )
        
        return response
