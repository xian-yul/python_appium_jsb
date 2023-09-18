import allure

from common.readelement import Element
from page.Apppage import AppPage
from utils.log import Log
from utils.times import sleep

userPage = {'splash_page': '.ui.activity.SplashActivity', 'home_page': '.ui.activity.MainActivity',
            'login_page': '.ui.activity.LoginNewActivity'}

user = Element('userPage')
log = Log()


class TestUser(AppPage):

    def user_login(self):
        with allure.step('1.启动金塑宝买家APP'):
            while self.return_current_activity() != userPage['home_page']:
                log.info('未到主界面')
                sleep(2)
                if self.return_current_activity() == userPage['home_page']:
                    log.info('已到主界面')
                    break;
        with allure.step('2.跳转登录界面,依次输入账号 、验证码'):
            sleep(0.5)
            self.is_click(user['home_me'])
            self.driver.implicitly_wait(5)
            self.input_text(user['user_login_phone'], '13500135000')
            self.is_click(user['user_login_code_btn'])
            self.input_text(user['user_login_code_text'], '666666')
            self.is_click(user['user_login_btn'])
            sleep(0.5)
        with allure.step('3. 验证是否登录成功'):
            try:
                assert self.return_current_activity() == userPage['home_page']
                log.info('登录成功')
                self.driver.close_app()
            except AssertionError:
                self.save_screenshot()
                log.error('断言错误')
