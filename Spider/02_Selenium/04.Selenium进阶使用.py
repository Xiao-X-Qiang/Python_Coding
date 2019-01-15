
from selenium import webdriver
import time

driver = webdriver.Chrome()
#
driver.get("https://www.qiushibaike.com/text/")

ret1 = driver.find_element_by_xpath("//div[@id=\"content-left\"]/div")  # 返回的是一对象，没有则报错

ret2 = driver.find_elements_by_xpath("//div[@id=\"content-left\"]/div")  # 返回的是对象列表，没有，则为空列表，推荐使用

print("ret1:",type(ret1))
print("*"*25)

print("ret2:",ret2)
for i in ret2:
    # print(i.find_element_by_xpath("./a[1]//div[@class='content'][1]").text)  # 获取文本
    print(i.find_element_by_xpath("./a[1]").get_attribute("href"))  # selenium会自动补全地址，获取属性

driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=39042058_27_oem_dg&wd=%E7%B3%97%E7%99%BE%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90&rsv_pq=b5634616000171a9&rsv_t=3a24MqYfhiV9QS2iZIdk72gETq5gcPXw6TSmAkTr5VncBK2NnX7r4bzPkyk1kxsrnswly6%2BWlei2&rqlang=cn&rsv_enter=1&rsv_sug3=9&rsv_sug1=6&rsv_sug7=101&sug=%25E7%25B3%2597%25E7%2599%25BE%25E7%25BB%258F%25E5%2585%25B8%25E6%25AE%25B5%25E5%25AD%2590&rsv_n=1")
href = driver.find_element_by_link_text("下一页>").get_attribute("href")  # 完全匹配
href1 = driver.find_element_by_partial_link_text("下一").get_attribute("href")  # 部分匹配即可
print(href)
print(href1)


time.sleep(5)
driver.quit()