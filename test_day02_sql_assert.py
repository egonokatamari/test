import pytest
import requests
import pymysql

def test_update_user_nickname():
    #1.模拟请求：修改用户昵称为“大漠孤烟”
    url = "https://httpbin.org/post"
    new_name = "大漠孤烟"
    res = requests.post(url,json={"user_id":1,"nickname":new_name})

    # 接口断言
    assert res.status_code == 200

    #2.数据库层断言(双层校验的核心)
    db = pymysql.connect(host="localhost",user="root",passwd="123456",db="test_db")
    cursor = db.cursor()
    try:
        # 这里用UPDATE模拟我本地真实的数据操作
        cursor.execute("update t_user set nickname=%s where id=1",(new_name,))
        db.commit()

        # 查库校验：刚改的数据到底落库没有？
        cursor.execute("select nickname from t_user where id = 1")
        result = cursor.fetchone()
        assert result[0] == new_name
    finally:
        # 先关闭cursor再关闭db
        cursor.close()
        db.close()