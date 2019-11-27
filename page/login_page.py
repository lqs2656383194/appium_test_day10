"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    def input_username(self,name):
        self.input_func(page.username,name)
    def input_password(self,password):
        self.input_func(page.pwd,password)
    def click_login_btn(self):
        self.click_func(page.login_btn)
    def click_con_btn(self):
        self.click_func(page.con_btn)
    def get_nick_name(self):
        """获取昵称"""
        return self.get_text_func(page.nick_name)

