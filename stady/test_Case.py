from selenium import webdriver
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('http://192.168.3.20:9010/#/user/login')
    driver.maximize_window()  # 窗口最大化
    driver.implicitly_wait(10)  # 隐式等待10s
    print('测试运行前脚本')
    yield driver
    # sleep(1)
    driver.quit()
    print('测试运行后脚本')


@pytest.fixture
def start():
    start = webdriver.Chrome()
    start.get('http://192.168.3.20:9010/')
    start.maximize_window()  # 窗口最大化
    start.implicitly_wait(10)  # 隐式等待10s
    start.find_element_by_id('userName').send_keys('hmgf')
    start.find_element_by_id('password').send_keys('hmgf600987')
    start.find_element_by_xpath \
        ("//*[text()='登 录']").click()
    print('测试运行前脚本')
    yield start
    # sleep(1)
    start.quit()
    print('测试运行后脚本')


def test_case_ok(driver):  # 正向用例
    driver.find_element_by_id('userName').send_keys('hmgf')
    driver.find_element_by_id('password').send_keys('hmgf600987')
    driver.find_element_by_xpath \
        ("//*[text()='登 录']").click()
    sleep(0.5)
    msg = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/span[2]').text
    print(msg)
    assert msg == '登录成功!'  # 断言


def test_case_no(driver):  # 反向用例
    driver.find_element_by_id('userName').send_keys('233')
    driver.find_element_by_id('password').send_keys('12345')
    driver.find_element_by_xpath \
        ("//*[text()='登 录']").click()
    sleep(0.5)
    msg = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/span[2]').text
    print(msg)
    assert msg == '用户不存在!'  # 断言


def test_case(start):  # 登录之后的操作
    start.find_element_by_xpath('//*[text()="设备管理"]').click()
    start.find_element_by_link_text('设备实例').click()
    start.find_element_by_xpath('//span//input[@type="search"]').click()
    start.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div').click()


if __name__ == '__main__':
    pytest.main()
