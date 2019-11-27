from appium import webdriver


def init_driver():
    """驱动对象获取方法"""

    # 3.声明启动参数
    capabilities = {
        "platformName": "Android",  # 平台类型(iOS 或 Android)
        "platformVersion": "5.1",  # 手机系统版本
        "deviceName": "模拟器",  # 设备名称(模拟器 或 真机)
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测引用的包名
        "appActivity": ".MainActivity",  # 应用的启动名
        "resetKeyboard": True,
        "unicodeKeyboard": True
        # "noReset":True  不重置应用状态
    }

    # 待测应用：通讯录的包名和启动名
    # com.android.contacts/.activities.PeopleActivity

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver


if __name__ == '__main__':
    init_driver()
