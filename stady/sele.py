from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')

s1 = Select(driver.find_element(By.ID,'s1Id'))  # 实例化Select

s1.select_by_index(1)  # 选择第二项选项：o1
sleep(1)
s1.select_by_value("o2")  # 选择value="o2"的项
sleep(1)
s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本


s2 = Select(driver.find_element(By.ID,'s3Id'))
sleep(1)
s2.select_by_value('o3val')
sleep(1)
s2.select_by_visible_text('With spaces')
# driver.quit()
