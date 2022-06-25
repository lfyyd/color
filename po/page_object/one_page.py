from selenium.webdriver.common.by import By

from po.base.base_page import BasePage


class OnePage(BasePage):
    url = 'http://192.168.3.20:9010/#/dashboard/analysis'
    sb = (By.XPATH, '//*[@id="root"]/div/div/section/aside/div/ul/li[2]/div/span/span/span[2]')
    sl = (By.LINK_TEXT, '设备实例')
    ssk = (By.XPATH,
           '//*[@id="root"]/div/div/section/section/div/main/div/div/div/div/div/div[2]/div/div[1]/div/div['
           '1]/span/span/span[1]/input')
    qd = (By.XPATH, '//*[@id="root"]/div/div/section/section/div/main/div/div/div/div/div/div[2]/div/div[1]/div/div['
                    '1]/span/span/span[2]')

    def one(self, content):
        self.geturl(self.url)
        self.click(self.sb)
        self.click(self.sl)
        self.input(self.ssk, content)
        self.click(self.qd)
