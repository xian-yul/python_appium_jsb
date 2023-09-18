import time
import pytest
from appium import webdriver

from conftest import android_setting

driver = None


# 启动安卓系统中的金塑宝app
@pytest.fixture()
def start_app():
    global driver
    print('123')
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', android_setting)
    return driver


# 关闭安卓系统中的金塑宝app
@pytest.fixture()
def close_app():
    yield driver
    time.sleep(2)
    driver.close_app()
