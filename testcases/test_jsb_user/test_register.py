import allure
from selenium.webdriver.common.by import By


@allure.epic('安卓买家端用户注册')
class TestRegister():
    @allure.story('注册')
    @allure.title('[case01] 验证安卓买家登录')
    def test_case01(self, start_app, close_app):
        with allure.step('1. 启动安卓系统中的金塑宝app'):
            driver = start_app
        with allure.step('2.依次输入账号 、验证码'):
            driver.implicitly_wait(20)
            driver.find_element(By.XPATH, "//*[@text='我的']").click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'cn.jinsubao.app:id/et_phone').send_keys('13500135000')
            driver.find_element(By.ID, 'cn.jinsubao.app:id/cv_code').click()
            driver.find_element(By.ID, 'cn.jinsubao.app:id/et_code').send_keys('666666')
            driver.implicitly_wait(50)
            driver.find_element(By.ID, 'cn.jinsubao.app:id/btn_login').click()
        with allure.step('3. 验证是否登录成功'):
            print(1)
            driver = close_app
