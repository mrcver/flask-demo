import logging
from logging import FileHandler
from app import app
from app.config import LOG_FILE

# web服务启动入口文件
if __name__ == '__main__':
    # 日志句柄
    fh = FileHandler(LOG_FILE)
    # 日志级别
    fh.setLevel(logging.DEBUG)
    # 进程日志输出到文件
    app.logger.addHandler(fh)
    # 方便本地测试时指定端口
    app.debug = True
    app.run(host='0.0.0.0', port=9529)
    # app.debug = False
    # app.run()
