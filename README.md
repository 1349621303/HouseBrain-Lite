# HouseBrain-Lite项目
### 软件工程基础作业的项目文档&组内学习笔记

> This is a smart room monitoring system developed based on the Flask framework and OpenCV technology, using the Raspberry Pi as a server to deploy the project.
 
# 项目大体框架 from lgx
 
| 安装指令(或在PyCharm中直接安装插件) | 用途                            | 版本号 |
| ----------------------------------- | ------------------------------- | ------ |
| flask-blueprint                     | 蓝图，用于将后端逻辑部分分开    |        |
| Flask-Migrate                       | 迁移仓库，用于更新Model时更方便 |        |
| Flask-Script                        | Flask脚本                       |        |
| Flask-SQLAlchemy                    | 一种用于Flask的ORM框架          |        |
| PyMySQL                             | python的MySQL插件               |        |


> 生成迁移仓库(migration)的三句命令行：
>
> ```shell
> # 第一次执行这三个语句，之后如果需要更新数据库的内容只需要执行后两行语句
> python manage.py db init
> python manage.py db migrate
> python manage.py db upgrade
> ```
>
> 如果数据库迁移Target database is not up to date报错，删掉migration之后重新执行上述三句命令行即可(如果使用sqlite数据库还要删除.sqlite文件)
>
> migration的生成有时候可能会比较慢，如果执行上述三句命令行没有生成migration文件，建议重新启动项目，或者等待片刻
>
> 如果有“ImportError: No module named 'MySQLdb'”报错，是因为python2和python3在数据库模块支持这里存在区别，python2是mysqldb，而到了python3就变成mysqlclient，pip install mysqlclient即可。因为现有学习资料(尤其是网课)很多的flask教程都是基于python2的，所以难免会有一些差异

```
# 史上最坑问题，现在也不清楚究竟是怎么回事，是FLASK_ ENV而不是FLASK_ENV
# python中os模块获取环境变量的一个方法，FLASK_ ENV为flask中内置的配置变量
env = os.environ.get("FLASK_ ENV", "develop")
```

# 宿舍视频流实现 form lwl
主要技术：
- opencv
- 深度学习
- 请求处理

## 主要实现功能

### 视频监控
发现行人可以及时检测出，并且圈出这些人
关于与后端的接口交互问题，建议开启跨域访问，留下相关接口。我可以直接在监控模块中留下可以发出请求的函数

### 人脸识别开门
使用opencv进行图片收集，DL进行人脸识别
准确率较高。
问题：需要进行硬件模拟

### 关于宿舍卫生状况提醒
使用深度学习制作的图片分类问题，能够较精确的判断宿舍是干净还是比较脏。
目前设想是每天固定时间段对宿舍进行卫生，如果检测判定为脏，那么就发送邮件等提醒给用户，并且附上图片
- 使用kaggle上的数据
- cnn卷积神经网络，正则化，图像增强防止过拟合
- 迁移学习（考虑到性能，还是不用为好）
目前在较低的内存开销下，能够实现80%的正确率。















