import requests
from lxml import etree
import time
from queue import Queue
from threading import Lock
import threading
import random
import json

# 从西刺代理获取免费代理IP,并进行验证
# 采用多线程，并以Queue进行线程间数据的流动
# 在主程序进行了延时操作(请求响应较慢，此时三队列为空，程序结束)
# 为了避免多次打开文件，在实例化时打开了文件，并对多线程文件写进行了加锁操作，注意，文件必须关闭，内容才可正确写入，故也要作异常处理
# 参考示例：01_requests-->16.spider_qiushibaike_multi_threading


class SpiderIP(object):
    def __init__(self):

        user_agents = [
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        ]

        self.url = "https://www.xicidaili.com/nn/"
        self.header = {
            "User-Agent":random.choice(user_agents)
        }

        self.lock = Lock()

        self.f = open("./proxies_xicidaili.txt", "a", encoding="utf8")

        self.html_queue = Queue()
        self.proxies_queue = Queue()
        self.enable_proxies = Queue()

    def get_proxies(self):
        while True:
            element = self.html_queue.get()
            tr_list = element.xpath('//table[@id="ip_list"]//tr[position()>1]')
            for tr in tr_list:
                IP = tr.xpath('./td[2]/text()')[0]
                Port = tr.xpath('./td[3]/text()')[0]
                Cate = tr.xpath('./td[6]/text()')[0]
                proxies = Cate + "://" + IP + ":" + Port
                self.proxies_queue.put(proxies)
                print(proxies)
            self.html_queue.task_done()

    def verify_proxies(self):
        while True:
            proxies = self.proxies_queue.get()

            proxies = {proxies.split(":", 1)[0]: proxies}
            print(proxies)

            response = requests.get("http://www.baidu.com", headers=self.header, proxies=proxies)

            if response.status_code == 200:
                self.enable_proxies.put(proxies)

            self.proxies_queue.task_done()

    def save_proxies(self):
        while True:

            proxies = self.enable_proxies.get()
            self.lock.acquire()
            self.f.write(json.dumps(proxies,ensure_ascii=False))
            self.f.write("\n")
            self.lock.release()

            self.enable_proxies.task_done()

    def get_element(self):

        next_url = True
        while next_url:
            time.sleep(random.random())
            response = requests.get(self.url, headers=self.header)
            html = response.content.decode()
            element = etree.HTML(html)
            self.html_queue.put(element)
            next_url = element.xpath("//a[contains(text(),'下一页 ›')]/@href")

            if len(next_url) > 0:
                next_url = "https://www.xicidaili.com" + next_url[0]
                self.url = next_url
            else:
                next_url = False

    def run(self):

        try:
            t_list = []

            t0 = threading.Thread(target=self.get_element)
            t_list.append(t0)

            t1 = threading.Thread(target=self.get_proxies)
            t_list.append(t1)

            t2 = threading.Thread(target=self.verify_proxies)
            t_list.append(t2)

            t3 = threading.Thread(target=self.save_proxies)
            t_list.append(t3)

            for i in t_list:
                i.setDaemon(True)
                i.start()

            time.sleep(5)  # 加延时，因为请求响应较慢，此时三个队列为空，程序会结束，故而子程序加延时以便请求队列中有内容

            for q in [self.html_queue, self.proxies_queue, self.enable_proxies]:
                q.join()
        except Exception as result:
            print(result)
        else:
            self.f.close()
            print("主线程结束")
        finally:
            self.f.close()


def main():
    spiderip = SpiderIP()
    spiderip.run()


if __name__ == '__main__':
    main()
