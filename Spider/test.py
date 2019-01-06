
import requests
import re
import json

def main():

    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

    post_data = {"url": "https://98.91p12.space/view_video.php?viewkey=9eb6c92a16a9d6f9fdf6&page=24&viewtype=basic&category=mr"}

    res = requests.post("https://www.vlogdownloader.com/download.html", headers=headers, data=post_data)

    res = res.content.decode()

    ret = re.findall("<script>var props=(.*?)</script>", res)[0]

    ret1 = json.loads(ret)

    print(ret)

    # ret1 = json.loads(ret)





if __name__ == "__main__":
    main()
