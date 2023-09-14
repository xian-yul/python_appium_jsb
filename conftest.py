# 配置app的各种连接信息
import pytest


@pytest.fixture(scope='session')
def android_setting():
    des = {
        'automationName': 'appium',
        'platformName': 'Android',
        'platformVersion': '13',  # 系统版本
        'deviceName': 'RMX3770',  # 设备名称
        'appPackage': 'cn.jinsubao.app',  # 启动APP的包名
        'appActivity': '.ui.activity.SplashActivity',  # 启动的Activity名称
        # 'udid': '127.0.0.1:4723',  # 通过命令行 adb devices 可查看到的udid
        'noReset': True,  # 是否重置APP
        'noSign': True,  # 是否不签名
        'unicodeKeyboard': True,  # 是否支持中文输入
        'resetKeyboard': True,  # 是否支持重置键盘
        'newCommandTimeout': 30  # 30秒没发送新命令就断开连接
    }
    return des
