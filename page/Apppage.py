import time

from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from config.conf import cm
from conftest import android_setting
from utils.times import sleep


class AppPage(object):
    """selenium基类"""

    def __init__(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_setting())
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def by_uiautomator(self, uiautomator):
        return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator)

    def is_element(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return AppPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return AppPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        #   log.info("相同元素：{}".format((locator, number)))
        return number

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        #  log.info("获取文本：{}".format(_text))
        return _text

    def return_current_activity(self):
        """返回当前页面 activity"""
        return self.driver.current_activity

    def input_text(self, locator, txt):
        """文本输入"""
        ele = self.find_element(locator)
        ele.clear()
        sleep(0.2)
        ele.send_keys(txt)

    def save_screenshot(self):
        """当前页面截图"""
        self.driver.save_screenshot("./{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    def drag(self, bx=0.50, bw=0.05, by=0.4, bz=0.9):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        sx = x * bx
        ex = x * bw
        sy = y * by
        ey = y * bz
        return self.driver.swipe(sx, sy, ex, ey, 1000)
