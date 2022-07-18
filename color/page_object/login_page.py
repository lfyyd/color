import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from color.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://192.168.3.20:8065/#/user/login/'
    user = (By.ID, 'username')
    word = (By.ID, 'password')
    btn = (By.XPATH, '//*[text()="登 录"]')

    def login(self, username, password):
        self.geturl(self.url)
        self.input(self.user, username)
        self.input(self.word, password)
        self.click(self.btn)
        # self.jietu()

