import pytest
from selenium import webdriver

from color.data.loadyaml import loadyaml
from color.page_object.login_page import LoginPage
from color.page_object.color_page import ColorPage


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('admin','123456')
    yield driver
    driver.quit()


@pytest.mark.smoke
@pytest.mark.parametrize('udata', loadyaml('./color/data/user.yaml'))
def test_01(udata):
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login(udata['usr'], udata['pwd'])
    ast = lp.asser()
    print(ast)
    assert ast == udata['assert']


@pytest.mark.parametrize('udata', loadyaml('./color/data/color.yaml'))
def test_02(udata, driver):
    cr = ColorPage(driver)
    cr.color(udata['name'], udata['l'], udata['a'], udata['b'])
    ast = cr.asser()
    print(ast)
    assert ast == udata['assert']
