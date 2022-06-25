

from color.base.base_page import BasePage
from selenium.webdriver.common.by import By


class ColorPage(BasePage):
    url = 'http://192.168.32.120:8085/#/color/fastsearch'
    dj = (By.PARTIAL_LINK_TEXT, "色彩列表")
    tj = (By.XPATH, "//*[text()='添加新名称']")
    mc = (By.ID, 'name')
    l = (By.ID, 'l')
    a = (By.ID, 'a')
    b = (By.ID, 'b')
    btn = (By.XPATH,'//*[text()="添 加"]')

    def color(self, name, l, a, b):
        self.wait(self.dj)
        self.click(self.dj)
        self.wait(self.tj)
        self.click(self.tj)
        self.wait(self.mc)
        self.input(self.mc, name)
        self.input(self.l, l)
        self.input(self.a, a)
        self.input(self.b, b)
        self.click(self.btn)


