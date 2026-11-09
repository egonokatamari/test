import pymysql

# 创建数据库连接
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="test"
    )


# 查询一条数据
def query_one(sql, params=None):
    db = get_connection()
    cursor = db.cursor()

    try:
        cursor.execute(sql, params)
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        db.close()


# 执行增删改
def execute_sql(sql, params=None):
    db = get_connection()
    cursor = db.cursor()

    try:
        cursor.execute(sql, params)
        db.commit()
    finally:
        cursor.close()
        db.close()