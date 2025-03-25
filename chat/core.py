"""
chat 核心模块
"""

import requests
import json
import time
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from log.logger import logger
from core.constants import CHAT_ENDPOINT

def chat_core(api_key, request_data):
    start_time = time.time()
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    is_stream = request_data.get("stream", False)
    
    try:
        if is_stream:
            request_data["stream"] = True
            
            response = requests.post(CHAT_ENDPOINT, headers=headers, json=request_data, stream=True)
            
            if response.status_code != 200:
                error_msg = f"聊天请求失败: HTTP {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data and isinstance(error_data["error"], dict):
                        error_msg = error_data["error"].get("message", error_msg)
                    elif "message" in error_data:
                        error_msg = error_data["message"]
                    if "code" in error_data:
                        error_msg = f"错误 {error_data['code']}: {error_msg}"
                except:
                    pass
                
                logger.error(f"流式聊天请求失败: {error_msg}")
                response.close()
                raise HTTPException(status_code=response.status_code, detail=error_msg)
            
            def generate():
                first_chunk_received = False
                first_chunk_time_diff = 0
                input_tokens = 0
                output_tokens = 0
                
                try:
                        
                    for line in response.iter_lines():
                        if line:
                            if not first_chunk_received:
                                first_chunk_time = time.time()
                                first_chunk_time_diff = first_chunk_time - start_time
                                first_chunk_received = True
                            
                            line_data = line.decode('utf-8')
                            
                            try:
                                if line_data.startswith("data: "):
                                    data_json = json.loads(line_data[6:])
                                    if "usage" in data_json:
                                        usage = data_json["usage"]
                                        input_tokens = usage.get("prompt_tokens", input_tokens)
                                        output_tokens = usage.get("completion_tokens", output_tokens)
                            except:
                                pass
                            
                            yield f"{line_data}\n\n"
                
                finally:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    
                    output_time = elapsed_time - first_chunk_time_diff if first_chunk_received else elapsed_time
                    tokens_per_second = output_tokens / output_time if output_time > 0 and output_tokens > 0 else 0
                    
                    logger.info(f"首字时间: {first_chunk_time_diff:.2f}秒, 总共耗时: {elapsed_time:.2f}秒, 输入token: {input_tokens}, 输出token: {output_tokens}, 平均输出速度: {tokens_per_second:.2f} tokens/秒")
            
            return StreamingResponse(generate(), media_type="text/event-stream")
        else:
            response = requests.post(CHAT_ENDPOINT, headers=headers, json=request_data, timeout=60)
            
            if response.status_code != 200:
                try:
                    error_data = response.json()
                    if "error" in error_data and isinstance(error_data["error"], dict):
                        error_msg = error_data["error"].get("message", f"请求失败: HTTP {response.status_code}")
                    elif "message" in error_data:
                        error_msg = error_data["message"]
                    else:
                        error_msg = f"请求失败: HTTP {response.status_code}"
                    
                    if "code" in error_data:
                        error_msg = f"错误 {error_data['code']}: {error_msg}"
                except:
                    error_msg = f"请求失败: HTTP {response.status_code}"
                
                logger.error(f"Chat API请求失败: {error_msg}")
                raise HTTPException(status_code=response.status_code, detail=error_msg)
            
            response_json = response.json()
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            input_tokens = 0
            output_tokens = 0
            
            if "usage" in response_json:
                input_tokens = response_json["usage"].get("prompt_tokens", 0)
                output_tokens = response_json["usage"].get("completion_tokens", 0)
            
            tokens_per_second = output_tokens / elapsed_time if elapsed_time > 0 and output_tokens > 0 else 0
            
            logger.info(f"首字时间: 0, 总共耗时: {elapsed_time:.2f}秒, 输入token: {input_tokens}, 输出token: {output_tokens}, 平均输出速度: {tokens_per_second:.2f} tokens/秒")
            
            return response_json
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API 请求异常: {str(e)}")
        raise HTTPException(status_code=500, detail=f"聊天请求处理失败: {str(e)}")
