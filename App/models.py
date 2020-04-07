from App.ext import db

# 用户数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 用户名称
    password = db.Column(db.String(100))  # 密码
