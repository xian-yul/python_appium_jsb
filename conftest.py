# 配置app的各种连接信息
import pytest


def android_setting():
    des = dict()
    des['automationName'] = 'appium'
    des['platformName'] = 'Android'
    des['platformVersion'] = '13'  # 系统版本
    des['deviceName'] = 'RMX3770'  # 设备名称
    des['appPackage'] = 'cn.jinsubao.app'  # 启动APP的包名
    des['appActivity'] = '.ui.activity.SplashActivity'  # 启动的Activity名称
    des['noReset'] = True  # 是否重置APP
    des['noSign'] = True  # 是否不签名
    des['unicodeKeyboard'] = True  # 是否支持中文输入
    des['resetKeyboard'] = True  # 是否支持重置键盘
    des['newCommandTimeout'] = 30  # 30秒没发送新命令就断开连接
    return des
