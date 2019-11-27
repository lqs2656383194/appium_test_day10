"""
登录-测试用例
"""
from common.utils import init_driver
from page.page_factroy import PageFactory


class TestLogin(object):
    """登录测试方法"""

    def setup_class(self):
        # 驱动对象的获取
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

    def teardown_class(self):
        """退出驱动对象"""
        self.driver.quit()

    def test_login(self):
        """登录测试方法"""
        # 点击我的
        self.page_factory.home_page.click_mine_page()
        # 点击登录、注册
        self.page_factory.mine_page.click_login()
        # 输入账号
        self.page_factory.login_page.input_username('17611175311')
        # 输入密码
        self.page_factory.login_page.input_password('shuang0619')
        # 点击登录按钮
        self.page_factory.login_page.click_login_btn()
        # 点击签到确定按钮
        self.page_factory.login_page.click_con_btn()
        # 获取昵称
        nick_name = self.page_factory.login_page.get_nick_name()
        print('昵称是', nick_name)
        # 断言判断结果
        assert '用户_243' in nick_name
