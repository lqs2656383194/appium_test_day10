"""
主页页面
"""
import page
from base.base_page import BasePage


class HomePage(BasePage):
    def click_mine_page(self):
        self.click_func(page.mine)