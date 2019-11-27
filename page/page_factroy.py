"""
工厂方法
"""
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactroy(object):
    def __init__(self,driver):
        self.driver=driver
    def home_page(self):
       return  HomePage(self.driver)
    def mine_page(self):
        return MinePage(self.driver)
    def login_page(self):
        return LoginPage(self.driver)