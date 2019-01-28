


# from multiprocessing import Pool, Queue
# import multiprocessing
# import time
#
#
# def function1(i, q):
#     time.sleep(1)
#     print("sub+%d" % i)
#
#
# if __name__ == "__main__":
#     q = multiprocessing.Manager().Queue()
#     pool = Pool(5)
#
#     for i in range(10):
#         pool.apply_async(function1, args=(i, q))
#     pool.close()
#     pool.join()
#     print('end')


# temp = "HTTP://59.56.168.220:9999"
# a= temp.split(":",1)[0]
# b = temp.split(":",1)[1]
#
# print(a,b)



import requests
from lxml import etree
import random


user_agents = [
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
]

url = "https://www.xicidaili.com/nn/"
header = {
    "User-Agent": random.choice(user_agents)
}


response = requests.get(url, headers=header)
html = response.content.decode()
element = etree.HTML(html)

next_url = element.xpath("//a[contains(text(),'下一页 ›')]/@href")[0]
print(next_url)