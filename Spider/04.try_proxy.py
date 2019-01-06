
import requests

proxy = {"http": "http://106.14.176.162:80"}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

r = requests.get("http://www.baidu.com", headers=headers, proxies=proxy)
print(r.status_code)