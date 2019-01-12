
import requests
import re
import json


# 程序虽然未能运行，止步于异步加载数据，有待于进一步考究
# 更注重于逻辑的安排，其次才是代码的实现
# 注意变量名的使用
# 同一功能（保存结果）有不同的实现细节，所以分别定义了

class Neihan(object):
    def __init__(self):
        self.start_url = "http://neihanshequ.com"
        self.next_url_temp = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content(self, html_str):
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html_str, re.S)
        max_time = re.findall(r"max_time:(.*?)", html_str)[0]
        return content_list, max_time

    def get_content_list(self, json_str):  # 从json_str中提取数据
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]["data"]
        content_list = [i["group"]["content"] for i in data]
        max_time = dict_ret["data"]["max_time"]
        has_more = dict_ret["data"]["has_more"]
        return content_list, max_time, has_more

    def save_content_list(self, content_list):
        with open("neihan.txt", "a", encoding="utf8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):
        # 1.start_url
        # 2.请求，获得响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        content_list, max_time = self.get_first_page_content(html_str)
        # 4.保存
        self.save_content_list(content_list)

        has_more = True  # 默认有第二页
        while has_more:
            # 5.构造第二页url
            next_url = self.next_url_temp.format(max_time)
            # 6.发送请求，获取响应
            json_str = self.parse_url(next_url)
            # 7.提取数据
            content_list, max_time, has_more = self.get_content_list(json_str)
            # 8.保存
            self.save_content_list(content_list)

        # 9.循环5-8


def main():
    neihan = Neihan()
    neihan.run()


if __name__ == '__main__':
    main()
