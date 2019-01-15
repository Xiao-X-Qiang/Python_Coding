import requests
import json
import sys


class FanYi(object):
    def __init__(self):
        self.post_url = "https://fanyi.baidu.com/basetrans"
        self.post_headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def get_url(self):
        post_data = {
            # "query": "人生苦短，我用python",
            "query": sys.argv[1],
            "from": "zh",
            "to": "en"
        }
        return post_data

    def run(self):
        # 1.获取url
        post_data = self.get_url()
        response = requests.post(self.post_url, data=post_data, headers=self.post_headers)
        # print(response.content.decode())
        print(json.loads(response.content.decode())["trans"][0]["dst"])


def main():
    fanyi = FanYi()
    fanyi.run()


if __name__ == "__main__":
    main()
