# HouseBrain-Lite

### `软件工程基础`作业的项目文档&组内学习笔记 from lgx

> This is a smart room monitoring system developed based on the Flask framework and OpenCV technology, using the Raspberry Pi as a server to deploy the project.

| 安装指令(或在PyCharm中直接安装插件) | 用途                            | 版本号    |
| ----------------------------------- | ------------------------------- | --------- |
| flask-blueprint                     | 蓝图，用于将后端逻辑部分分开    | 1.3.0     |
| **Flask-Migrate**                   | 迁移仓库，用于更新Model时更方便 | **2.5.3** |
| Flask-Script                        | Flask脚本                       | 2.0.6     |
| Flask-SQLAlchemy                    | 一种用于Flask的ORM框架          | 2.4.1     |
| **PyMySQL**                         | python的MySQL插件               | **0.9.3** |
| Jinja2                              | 模板引擎                        | 2.11.1    |
| Flask-Bootstrap                     | 用于引入Bootstrap               | 3.3.7.1   |

注意：**Flask-Migrate**和**PyMySQL**这两个版本不是用的最新版本，安装时请指定**标粗**的版本！

> 生成**迁移仓库**(migration)的三句命令行：
>
> ```shell
> python manage.py db init
> python manage.py db migrate
> python manage.py db upgrade
> ```
>
> 首先新建名为 ‘ **housebrainlite** ’ 的数据库，之后执行这三条语句，就可以生成数据库表结构啦（如下图）
>
> （PyCharm中的‘**Terminal**’中是写命令行的）
>
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200412000637500.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzU3NzY3NQ==,size_16,color_FFFFFF,t_70)
>
> 这里是执行三条命令行语句后生成的文件，以及数据库中的表结构
>
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200412000815410.png)
>
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200412000938997.png)

下面的是迁移仓库使用时的常见错误

> 如果数据库迁移Target database is not up to date报错，删掉migration之后重新执行上述三句命令行即可，
>
> 当然如果还是不好使，建议重启电脑，然后再开项目，毕竟也不是不可能（lgx碰过一次，卡了二十分钟）
>
> (如果使用sqlite数据库还要删除.sqlite文件)
>
> migration的生成有时候可能会比较慢，如果执行上述三句命令行没有生成migration文件，建议重新启动项目，或者等待片刻
>
> 如果有“ImportError: No module named 'MySQLdb'”报错，是因为python2和python3在数据库模块支持这里存在区别，python2是mysqldb，而到了python3就变成mysqlclient，pip install mysqlclient即可。因为现有学习资料(尤其是网课)很多的flask教程都是基于python2的，所以难免会有一些差异

最后收藏的一些比较好的和本项目有关的博客，不过有不少问题实际上也是书上找到的，这里推荐大家都有的一本书《Flask Web开发》（第二版），如果想看本书源码请进入该链接 https://github.com/miguelgrinberg/flasky 

[Python Flask-表单提交方式]: https://blog.csdn.net/Co_zy/article/details/76658862	"Python Flask-表单提交方式"
[数据库迁移Target database is not up to date报错]: https://blog.csdn.net/huang5487378/article/details/66973805
[pip 常用命令]: https://blog.csdn.net/sunlanchang/article/details/52563882
[Pycharm项目上传到Github]: https://blog.csdn.net/m0_37306360/article/details/79322947
[SQLAlchemy简明教程]: https://jiajunhuang.com/articles/2019_10_30-sqlalchemy.md.html
[Flask 环境变量 FLASK_APP 说明]: https://foofish.net/flask_app.html



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













