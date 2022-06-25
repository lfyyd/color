import pdb

from selenium.webdriver.common.by import By
from color.base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://192.168.32.120:8085/#/user/login/'
    user = (By.ID, 'username')
    word = (By.ID, 'password')
    btn = (By.XPATH, '//*[text()="登 录"]')

    def login(self, username, password):
        self.geturl(self.url)
        # pdb.set_trace()  # 调试
        self.input(self.user, username)
        self.input(self.word, password)
        self.click(self.btn)
        # self.sleep(0.1)
