"""
程序入口
"""

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from config.config import Settings
from core.initialization import initialize_app
from log.logger import logger

# 创建应用实例
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

# 配置
settings = Settings()

# 主程序入口
if __name__ == "__main__":
    initialize_app()
    port = settings.PORT
    logger.info("服务启动成功，监听端口: {}".format(port));
    app.run(host="0.0.0.0", port=port, debug=False)
