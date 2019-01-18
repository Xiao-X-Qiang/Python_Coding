from sys import argv
import requests, re, time, random, json


# 解析视频url，输出至video_url.txt

def random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))


f = open('./video_list.txt', mode='r+', encoding='utf8')
f1 = open('./video_url.txt', mode='a', encoding='utf8')

while True:
    line = f.readline()

    if not line:  # 判断是否到文件末尾
        break

    line = json.loads(line)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'X-Forwarded-For': random_ip(), 'referer': 'http://91porn.com'}
    url = line["href"]
    item = {}
    video_url = []
    content_html = requests.get(url=url, headers=headers)
    video_url = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>', str(content_html.content, 'utf-8', errors='ignore'))[0]

    item["title"] = line["title"]
    item["href"] = video_url

    f1.write(json.dumps(item,ensure_ascii=False))
    f1.write("\n")
    print(item)


print("解析完成")
f.close()
f1.close()
