"""
程序错误处理模块
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

def register_error_handlers(app: FastAPI):
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": {"message": exc.detail, "code": exc.status_code}}
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = exc.errors()
        error_details = []
        
        for error in errors:
            error_details.append({
                "loc": error["loc"],
                "msg": error["msg"],
                "type": error["type"]
            })
            
        return JSONResponse(
            status_code=422,
            content={"error": {"message": "请求参数验证失败", "code": 422, "details": error_details}}
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"error": {"message": "服务器内部错误", "code": 500}}
        )
