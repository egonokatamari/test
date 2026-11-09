import requests

def test_token_extract_and_pass():
    #1.模拟调登录接口拿到token
    login_res = requests.get("https://httpbin.org/uuid")
    token = login_res.json()["uuid"]

    #2.将token放入请求头，发给下一个接口
    headers = {"Authorization":f"Bearer {token}"}
    user_res = requests.get("https://httpbin.org/headers",headers=headers)

    assert user_res.json()["headers"]["Authorization"] == f"Bearer {token}"

def test_session_cookie_keep():
    # 使用session 自动记住cookie，不需要每次手动传
    session = requests.Session()

    # 接口1：种下cookie
    session.get("https://httpbin.org/cookies/set?my_cookie=hello_test")

    #接口2：直接请求，Session会自动携带刚才的cookie
    res = session.get("https://httpbin.org/cookies")
    assert res.json()["cookies"]["my_cookie"] == "hello_test"

