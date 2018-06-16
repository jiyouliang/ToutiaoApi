import pymysql


def get_connect(db):
    """连接mysql数据库"""
    connect = pymysql.connect(host="172.16.0.128", user="root",
                              passwd="mysql", db=db, charset="utf8")
    return connect
