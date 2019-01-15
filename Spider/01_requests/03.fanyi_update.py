
import requests
import json
import sys


class BaiduFanyi(object):

    def __init__(self, trans_str):
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.trans_str = trans_str
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):  # 提取翻译的结果
        ret = dict_response["trans"][0]["dst"]
        print("result is :", ret)

    def run(self):  # 实现主要逻辑
        # 1.获取语言类型
        # 1.1 准备post地址以及post_data
        lang_detect_data = {"query": self.trans_str}
        # 2.发送post请求，获取响应
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        # 1.3 提取语言类型

        # 2.准备post数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else {"query": self.trans_str,
                                                                                               "from": "en", "to": "zh"}
        # 3.发送请求，获取响应

        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4.撮翻译的结果
        self.get_ret(dict_response)


def main():
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()


if __name__ == "__main__":
    main()
