
from sys import argv
import requests, re, time, random


def random_ip():
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    d = random.randint(1, 255)
    return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))


f = open('./text.txt', mode='r+', encoding='utf8')
f1 = open('./dest.txt', mode='w+', encoding='utf8')
line = f.readline()
while line:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
        'X-Forwarded-For': random_ip(), 'referer': 'http://91porn.com'}
    url = line
    video_url = []
    base_req = requests.get(url=url, headers=headers)
    video_url = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>', str(base_req.content, 'utf-8', errors='ignore'))
    f1.writelines(video_url)
    f1.writelines('\n')
    line = f.readline()
f.close()
f1.close()

# 使用说明
# python3 1_91_mp4_url.py test.txt
# 会在当前目录下生成 dest.txt文件 ，里面包括所有的下载链接，可以使用迅雷或Downie下载



