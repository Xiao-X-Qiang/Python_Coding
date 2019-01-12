
from selenium import webdriver
import time

# 1.实例化Chrome浏览器
driver = webdriver.Chrome()

# 实例化PhantomJS浏览器实例,最新版的Selenium己警告该浏览器，(该浏览器己很久没有更新，但支持Chrome，Fox...)
# driver = webdriver.PhantomJS()

# 设置窗口大小
# driver.set_window_size(1366, 768)

# 2.发送请求
driver.get("http://www.baidu.com")

# 获取cookies
cookies = driver.get_cookies()
cookies_dict = {i["name"]:i["value"] for i in cookies}
print(cookies_dict)

# 获取HTML字符串
html_str = driver.page_source
# print(html_str)

# 截屏，更针对的是无界面浏览器
# driver.save_screenshot('./baidu.png')

# 元素定位的方法
driver.find_element_by_id("kw").send_keys("python")

# 点击事件-- 先定位元素，后触发事件
driver.find_element_by_id("su").click()

# 获取当前url地址，因为地址有可能跳转，比如百度搜索后，页面跳转
curl = driver.current_url
print(curl)

time.sleep(3)

# 3.关闭当前页面
driver.close()

# 退出浏览器
driver.quit()
