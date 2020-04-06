# # 应用包的构造文件
# # 引入Flask
# from flask import Flask
# # 引入Flask的BootStrap
# from flask_bootstrap import Bootstrap
# # 引入Flask提供的电子邮件支持
# from flask_mail import Mail
# # 引入SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
# # 引入config中的配置
# from app.config import envs
#==========================================分割线=====================================================

# Python中的日期类型引入
from datetime import timedelta
# 引入Flask
from flask import Flask
# 引入扩展模块
from app.extends import init_ext
# 引入配置模块
from app.config import envs
# 引入蓝图模块，有多少引入多少
from app.views.user import user

def create_app(env):
    #创建app,由主入口manage.py进行调用create_app
    app = Flask(__name__)

    #通过setting.py初始化此app
    app.config.from_object(envs.get(env))

    #注册蓝图
    app.register_blueprint(user)

    #初始化第三方扩展库，包括SQLAlchemy及Migrate等第三方库
    init_ext(app=app)

    #配置Flask-WTF，即设置session，通过加密或签名以不同的方式提升安全性
    app.config['SECRET_KEY'] = 'housebrain will change the world'
    # 设置session的保存时间
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    return app