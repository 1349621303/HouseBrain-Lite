def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "156354"
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    dbname = dbinfo.get("DBNAME") or "housebrainlite"
    # uri数据库+驱动://用户名:密码@主机:端口/具体哪一个库
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, dbname)

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# 开发环境
class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "156354",
        "HOST": "localhost",
        "PORT": "3306",
        "DBNAME": "housebrainlite"
    }

    # SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:156354@127.0.0.1:3306/housebrainlite'

