import allure
import pytest
from page_object.jsb_user_login import TestUser


@allure.epic('安卓买家端用户登录')
@allure.feature('V1.0版本')
class TestLogin:

    @allure.story('登录')
    @allure.title('[case01] 验证安卓买家登录')
    def test_user_login(self):
        user = TestUser()
        user.user_login()


if __name__ == '__main__':
    pytest.main(['testcases/test_login.py'])
