# from flask import Blueprint
#
# blue = Blueprint("first_blue",__name__)
#
# def init_first_blue(app):
#     app.register_blueprint(blueprint=blue)
#
# @blue.route('/')
# def index():
#     return 'Flask Index'
# =========================================分割线========================================================

# 引入hashlib，即摘要算法，可以对密码进行MD5加密
import hashlib
# 在这个user中依次引入Blueprint（蓝图，用于子系统的分离）、render_template（模板渲染）、
# session（用户对话）、redirect（重定向）、url_for（Flask中提供的URL生成函数）
from flask import Flask, Blueprint, render_template, session, redirect, url_for
# 这里注意要导入models中的models，而不是extends中的models
from app.models import db, User

# 申明一个蓝图对象user
user = Blueprint('user', __name__)

# 配置路由
@user.route('/')
def index():
    return render_template('index.html')
