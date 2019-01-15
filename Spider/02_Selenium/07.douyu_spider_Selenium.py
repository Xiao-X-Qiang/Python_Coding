
from selenium import webdriver
import time
import json

# 使用Selenium保存斗鱼直播的所有直播房间信息(https://www.douyu.com/directory/all)

class DouyuSpider(object):
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content(self):
        content_list = []
        room_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        for i in room_list:
            item = {}
            item["img_url"] = i.find_element_by_xpath(".//img[@class='JS_listthumb']").get_attribute("data-original")
            item["room_name"] = i.find_element_by_xpath("./a").get_attribute("title")
            item["live_cate"] = i.find_element_by_xpath(".//span[@class='tag ellipsis']").text
            item["anchor_name"] = i.find_element_by_xpath("//span[@class='dy-name ellipsis fl']").text
            item["room_hot"] = i.find_element_by_xpath(".//span[@class='dy-num fr']").text
            content_list.append(item)
            print(item)
        # 获取下一页的url地址，因为最后一页的下一页url地址和其它页的下一页的url地址class有所不同(selenium中class_name只能接受一个参数)
        # 当最后一页时，该next_url_temp将会是空列表，据此列表的长度可作判断；
        # 如果使用find_element_by_xpath时，当最后一页时，会报错
        next_url_temp = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url_temp[0] if len(next_url_temp) > 0 else None

        return content_list, next_url

    def save_content(self, content_list):
        with open("douyu.txt", "a", encoding="utf8") as f:
            for i in content_list:
                f.write(json.dumps(i, ensure_ascii=False))
                f.write("\n")

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.请求第一页数据
        self.driver.get(self.start_url)
        time.sleep(3)
        # 3.提取第一页的数据以及下一页的元素标签
        content_list, next_url = self.get_content()

        # 4.保存数据
        self.save_content(content_list)

        # 5.点击下一页，循环2-5
        while next_url is not None:  # 判断是否到达最后一页，否的话进入循环
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content()
            self.save_content(content_list)
        self.driver.page_source


def main():
    douyu = DouyuSpider()
    douyu.run()


if __name__ == '__main__':
    main()
