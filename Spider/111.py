
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.qiushibaike.com/text/")

while True:

    div_list = driver.find_elements_by_xpath("//div[@id='content-left']/div")

    for div in div_list:
        item = {}
        item["text"] = div.find_element_by_xpath("./a[1]//div[@class='content'][1]").text
        print(item["text"])
        print("*"*15)
    if len(driver.find_elements_by_class_name("next")) == 0:
        break
    driver.find_elements_by_class_name("next")[0].click()

    time.sleep(2)

time.sleep(5)

driver.quit()
