
from selenium import webdriver
import time

driver = webdriver.Chrome()
#
driver.get("https://mail.qq.com/")

driver.find_element_by_id("u").send_keys("451553616@qq.com")


time.sleep(5)
driver.quit()