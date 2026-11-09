import pytest
import pymysql

#定义一个fixture：专门用于测试前后的数据处理
@pytest.fixture
def temp_user():
    db = pymysql.connect(host="localhost",user="root",passwd="123456",db="test_db")
    cursor = db.cursor()

    # [yield之前：测试前置]造一条测试专属数据
    cursor.execute("insert into t_user (id,nickname) values (999,'临时用户')")
    db.commit()

    # 把造出来的用户ID丢给测试用例去用
    yield 999

    # [yield 之后：测试后置]不管用例成功还是失败，比执行数据清理
    cursor.execute("delete from t_user where id = 999")
    db.commit()
    cursor.close()
    db.close()
