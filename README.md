# HouseBrain-Lite项目【软件工程基础作业的项目文档&组内学习笔记】

> This is a smart room monitoring system developed based on the Flask framework and OpenCV technology, using the Raspberry Pi as a server to deploy the project.

| 安装指令(或在PyCharm中直接安装插件) | 用途                            | 版本号 |
| ----------------------------------- | ------------------------------- | ------ |
| flask-blueprint                     | 蓝图，用于将后端逻辑部分分开    |        |
| Flask-Migrate                       | 迁移仓库，用于更新Model时更方便 |        |
| Flask-Script                        | Flask脚本                       |        |
| Flask-SQLAlchemy                    | 一种用于Flask的ORM框架          |        |
| PyMySQL                             | python的MySQL插件               |        |
|                                     |                                 |        |
|                                     |                                 |        |





> 生成迁移仓库(migration)的三句命令行：
>
> ```shell
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

















