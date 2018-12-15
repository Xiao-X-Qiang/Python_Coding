
import gevent
import gevent.monkey

import urllib.request

gevent.monkey.patch_all()


def download(img_name, img_url):
   req = urllib.request.urlopen(img_url)
   data = req.read()
   with open(img_name, 'wb') as f:
       f.write(data)


def main():

    ge1 = gevent.spawn(download, '1.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/13/1931736_20181113121805_small.jpg")
    ge2 = gevent.spawn(download, '2.jpg', "https://rpic.douyucdn.cn/asrpic/181215/910907_796449_49c50_2_2249.jpg")

    # ge1.join()
    ge2.join()


if __name__ == "__main__":
    main()





