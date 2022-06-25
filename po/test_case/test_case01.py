import pytest
from selenium import webdriver
from po.page_object.login_page import LoginPage
from time import sleep

from po.page_object.one_page import OnePage


class Testone:

    def test_01(self):
        driver = webdriver.Chrome()
        lp = LoginPage(driver)
        sleep(1)
        lp.login('hmgf','hmgf600987')
        op = OnePage(driver)
        sleep(1)
        op.one('b28d9b84586b43dcb6fba00ad6878a16')



