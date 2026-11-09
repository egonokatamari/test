import pytest
import requests

# 准备数据
test_data = [
    ("admin","123456",200),
    ("","123456",200),
    ("admin","a"*100,200)
]

@pytest.mark.parametrize("username,password,expected_code",test_data)
def test_post_login(username,password,expected_code):
    url="https://httpbin.org/post"
    payload ={"username":username,"password":password}

    # 1.发送post请求
    res = requests.post(url,json=payload)

    #2.pytest 状态码断言
    assert res.status_code == expected_code # status_code是属性

    #3. 业务逻辑断言：验证传过去的数据被正确解析
    res_json = res.json() # 对响应体json化
    print(res_json["data"])
    assert res_json["json"]["username"] == username