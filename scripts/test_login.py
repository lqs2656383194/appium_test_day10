"""
登录-测试用例
"""
import pytest

from base.base_page import BasePage
from common.utils import init_driver
from page.page_factroy import PageFactory


class TestLogin(object):
    """登录测试方法"""

    def setup_class(self):
        # 驱动对象的获取
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)
        self.base_page = BasePage(self.driver)

    def teardown_class(self):
        """退出驱动对象"""
        self.driver.quit()

    @pytest.mark.parametrize("name,pwd,expect,is_success",
                             [(17611175311, 'shuang0619', '用户_243', True), ('', '123456', 'false', False)])
    def test_login(self, name, pwd, expect, is_success):
        """登录测试方法"""
        if is_success:  # 正向
            # 点击我的
            self.page_factory.home_page.click_mine_page()
            # 点击登录、注册
            self.page_factory.mine_page.click_login()
            # 输入账号
            self.page_factory.login_page.input_username(name)
            # 输入密码
            self.page_factory.login_page.input_password(pwd)
            # 点击登录按钮
            self.page_factory.login_page.click_login_btn()
            # 点击签到确定按钮
            self.page_factory.login_page.click_con_btn()
            # 获取昵称
            nick_name = self.page_factory.login_page.get_nick_name()
            print('昵称是', nick_name)
            # 断言判断结果
            assert expect in nick_name
        else:  # 反向
            # 按钮无法点击
            # 点击我的
            self.page_factory.home_page.click_mine_page()
            # 点击登录、注册
            self.page_factory.mine_page.click_login()
            # 输入账号
            self.page_factory.login_page.input_username(name)
            # 输入密码
            self.page_factory.login_page.input_password(pwd)
            # 点击登录按钮
            self.page_factory.login_page.click_login_btn()
            # 获取登录按钮的属性
            result = self.page_factory.login_page.get_login_btn_atr('clickable')
            print('获取的属性值', result)
            # 断言判断
            assert expect == result
        #     # 点击我的
        #     self.page_factory.home_page.click_mine_page()
        #     # 点击登录、注册
        #     self.page_factory.mine_page.click_login()
        #     # 输入账号
        #     self.page_factory.login_page.input_username(name)
        #     # 输入密码
        #     self.page_factory.login_page.input_password(pwd)
        #     # 点击登录按钮
        #     self.page_factory.login_page.click_login_btn()
        #     message = self.page_factory.login_page.get_toast()
        #     assert expect in message
