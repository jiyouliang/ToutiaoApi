import pymysql


def get_connect(db):
    """连接mysql数据库"""
    connect = pymysql.connect(host="192.168.1.100", user="root", passwd="12345678", db=db, charset="utf8")
    return connect
