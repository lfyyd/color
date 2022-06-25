from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def geturl(self, url):
        self.driver.get(url)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def asser(self):
        try:
            sleep(0.2)
            ast = self.driver.find_element(By.XPATH, '//div[contains(text(),"请输入")]')
            return ast.text
        except:
            sleep(0.2)
            ast = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/span[2]')
            return ast.text

    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(loc))
