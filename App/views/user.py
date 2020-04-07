# from flask import Blueprint
#
# blue = Blueprint("first_blue",__name__)
#
# def init_first_blue(App):
#     App.register_blueprint(blueprint=blue)
#
# @blue.route('/')
# def index():
#     return 'Flask Index'
# =========================================分割线========================================================

# 引入hashlib，即摘要算法，可以对密码进行MD5加密
import hashlib
# 在这个user中依次引入Blueprint（蓝图，用于子系统的分离）、render_template（模板渲染）、
# session（用户对话）、redirect（重定向）、url_for（Flask中提供的URL生成函数）
from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
# 这里注意要导入models中的models，而不是extends中的models
from App.models import db, User

# 申明一个蓝图对象user
userblue = Blueprint('userblue', __name__)

# 配置路由

@userblue.route('/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        result = User.query.filter(User.username == username,User.password == password).first()
        # 登录成功或者失败的判断
        if result:
            # 定义一个字典
            userItem = {}
            # 开始存数据
            userItem['username'] = result.username
            # session是http协议的状态跟踪技术，http协议是tcp短连接
            session['user'] = userItem
            # 登录成功，则保存Cookies信息
            # response = Response(render_template('indexmain',message='登录成功！'))
            # response = Response(redirect('indexmain'))
            # response.set_cookie('username', username, max_age=7 * 24 * 3600)
            # response.set_cookie('password', password, max_age=7 * 24 * 3600)
            # return response

            # return redirect(url_for('userblue.index'))
            return render_template('index.html')

        else:
            return render_template('login.html', message='用户名不存在或密码错误！')


# 查询用户
@userblue.route('/getuser')
def getuser():
    result = User.query.filter(User.username == 'lgx').first()
    return result.username

@userblue.route('/index')
def index():
    return render_template('index.html')

@userblue.route('/account')
def account():
    return render_template('account.html')







