import pymysql

from common.config import configs


def get_db():
    db = pymysql.connect(configs.get("db").get("ip"), configs.get("db").get("user"), configs.get("db").get("password"), configs.get("db").get("database"))
    return db

def insert(sql, params):
    # 打开数据库连接
    db = get_db()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.executemany(sql, params)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

def select(sql, param):
    # 打开数据库连接
    db = get_db()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql, param)
        result = cursor.fetchall()
        # 提交到数据库执行
        db.commit()
        return result
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()