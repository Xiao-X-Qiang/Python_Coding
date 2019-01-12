from selenium import webdriver
import time

from threading import Thread
from queue import Queue

import json


class Music_163(object):
    def __init__(self):
        self.url = "http://www.91porn.com/v.php?next=watch&page={}"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        # self.driver.set_window_size(1920, 1080)

        self.url_queue = Queue()


    def get_content(self, first_page,page_num):
        i = 0
        self.driver.get(self.url.format(first_page))
        while i<page_num:
            item = {}


            ret = self.driver.find_elements_by_xpath("//*[@id=\"videobox\"]/table/tbody/tr/td/div")
            for j in ret:
                item["title"] = j.find_element_by_xpath("./a").get_attribute("title")
                item["href"] = j.find_element_by_xpath("./a").get_attribute("href")
                self.url_queue.put(item)

            self.driver.find_element_by_partial_link_text("»").click()

            time.sleep(3)
            i += 1

    def save_list(self):
        while True:
            with open("./porn_url.txt", "a", encoding="utf8") as f:
                print("*" * 20)

                item = self.url_queue.get()
                print(item)
                f.write(json.dumps(item,ensure_ascii=False))
                f.write("\n")

            self.url_queue.task_done()

    def run(self):
        try:
            t_list = []

            t2 = Thread(target=self.get_content,args=(1,1,))  # 起始页，页码数，从第2页开始，下载2页
            t_list.append(t2)

            t3 = Thread(target=self.save_list)
            t_list.append(t3)

            for i in t_list:
                i.setDaemon(True)
                i.start()

            time.sleep(150)

            for q in [self.url_queue,]:
                q.join()

        finally:
            time.sleep(3)
            self.driver.quit()


def main():
    music_163 = Music_163()
    music_163.run()


if __name__ == '__main__':
    main()
