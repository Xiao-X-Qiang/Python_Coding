from selenium import webdriver
import time
import requests
import json
from threading import Thread

from queue import Queue

# Marionette	INFO	Listening on port 57184  日志出现此种问题，目前看来是由于版本的兼容问题，有待于进一步商榷

# 在该代码中，主要是熟悉使用selenium的基本用法 ，以及xpath在selenium中的使用
# TODO(修改该兼容性)


class Music_163(object):
    def __init__(self):
        self.url = "https://music.163.com/#"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        # self.driver.set_window_size(1920, 1080)
        self.driver.get(self.url)

        self.page_url_queue = Queue()  # 存放列表页地址
        self.list_url_queue = Queue()  # 存放歌单地址
        self.html_queue = Queue()  # 存放一个歌单的的html内容
        self.content_queue = Queue()  # 存放解析后的内容

    def get_page_url(self):
        while True:
            self.page_url_queue.put(self.driver.current_url)
            print(self.driver.current_url)
            self.driver.switch_to.frame("contentFrame")
            if self.driver.find_elements_by_partial_link_text("下一页")[0].get_attribute(
                    "href") != "javascript:void(0)":

                print("*" * 20)
                print(self.driver.find_elements_by_partial_link_text("下一页")[0].get_attribute("href"))

                self.driver.find_elements_by_partial_link_text("下一页")[0].click()
                print("*" * 20)

                self.driver.get(self.driver.current_url)
                time.sleep(3)
            else:
                break

    def get_list_url(self):
        while True:
            item = {}
            page_url = self.page_url_queue.get()
            driver_1 = webdriver.Chrome()
            driver_1.get(page_url)
            time.sleep(2)
            driver_1.switch_to.frame("contentFrame")

            ret1 = driver_1.find_elements_by_xpath("//ul[@id='m-pl-container']/li")
            for i in ret1:
                item["title"] = i.find_element_by_xpath(".//a").text
                item["href"] = i.find_element_by_xpath(".//a").get_attribute("href")
                self.list_url_queue.put(item)

            self.page_url_queue.task_done()

    def save_list(self):
        while True:
            with open("song_list.txt", 'a', encoding="utf8") as f:
                item = self.list_url_queue.get()
                print(item)
                f.write(json.dumps(item, ensure_ascii=False))
                f.write("\n")

                self.list_url_queue.task_done()



    def run(self):
        try:
            t_list = []

            self.driver.find_element_by_xpath("//a[@data-module='playlist']").click()  # 点击后，页面会跳转


            self.driver.switch_to.frame("contentFrame")  # 页面中有iframe，此时需要switch_to，方能定位元素

            self.driver.find_element_by_xpath("//a[@id='cateToggleLink']").click()  # url无变更，无需发请求
            self.driver.find_element_by_partial_link_text("华语").click()


            time.sleep(2)  # 重要，否则后面的xpath很有可能出错

            # self.get_page_url()

            t1 = Thread(target=self.get_page_url)
            t_list.append(t1)

            t2 = Thread(target=self.get_list_url)
            t_list.append(t2)

            t3 = Thread(target=self.save_list)
            t_list.append(t3)

            for i in t_list:
                i.setDaemon(True)
                i.start()

            for q in [self.page_url_queue, self.list_url_queue]:
                q.join()

        finally:
            time.sleep(3)
            self.driver.quit()


def main():
    music_163 = Music_163()
    music_163.run()


if __name__ == '__main__':
    main()
