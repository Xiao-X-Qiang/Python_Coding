
import requests
import retrying

headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

@retrying.retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    # print("*"*20)
    if method == "GET":
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
    else:
        response = requests.post(url, headrs=headers, timeout=3, data=data, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    finally:
        return html_str


if __name__ == "__main__":
    url = "https://www.baidu.com"
    res = parse_url(url)
    print(res)