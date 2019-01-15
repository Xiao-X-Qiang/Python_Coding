import requests
import re
import json

# 程序虽然未能运行，止步于异步加载数据，有待于进一步考究
# 更注重于逻辑的安排，其次才是代码的实现

class DoubanSpider(object):
    def __init__(self):
        self.start_url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18&loc_id=108288"

        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        dict_content = json.loads(json_str)
        content_list = dict_content["subject_collection_items"]
        total = dict_content["total"]
        return content_list,total

    def save_content(self,content_list):
        with open("douban.txt", "a", encoding="utf8") as f:
            for i in content_list:
                f.write(json.dumps(i))
                f.write("\n")

    def run(self):  # 实现主要逻辑
        # 1.构造开始url
        num = 0
        total = 1
        while num < total+18:
            url = self.start_url_temp.format(num)
            # 2.请求获取响应
            json_str = self.parse_url(url)

            # 3.获取数据
            content_list, total = self.get_content_list(json_str)

            # 4.保存数据
            self.save_content(content_list)

            # 5.构造下一页的url，进入循环2,3,4
            # if len(content_list) < 18:
            #     break
            num += 18



def main():
    douban_spider = DoubanSpider()
    douban_spider.run()


if __name__ == "__main__":
    main()
