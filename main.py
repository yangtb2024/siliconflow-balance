"""
程序入口
"""

from flask import Flask
from config.config import Settings
from core.initialization import initialize_app

# 创建应用实例
app = Flask(__name__)

# 配置
settings = Settings()

# 主程序入口
if __name__ == "__main__":
    initialize_app()
    port = settings.PORT
    print(f"服务启动在端口: {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
