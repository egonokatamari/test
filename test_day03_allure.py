import pytest
import allure
import requests

@allure.epic("核心业务中心")
@allure.feature("用户管理模块")
class TestUser:

    @allure.story("正向登陆测试")
    @allure.title("使用正确的账密应该登陆成功")
    def test_login_success(self):
        with allure.step("步骤1：准备测试数据"):
            payload = {"username":"root","pwd":"123456"}

        with allure.step("步骤2：发起登录接口请求"):
            res = requests.post("https://httpbin.org/post",json=payload)

        with allure.step("步骤3：断言状态码"):
            assert res.status_code == 200
