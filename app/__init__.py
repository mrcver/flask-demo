import pymysql
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, UPLOAD_FOLDER, MAX_CONTENT_LENGTH

app = Flask(__name__)

# 跨域
CORS(app, supports_credentials=True)

# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# mysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)

# 上传文件配置
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 上传目录
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH  # 上传大小

# 导入路由, 需放在底部，不然会产生依赖循环导入问题
from app.controller import index
