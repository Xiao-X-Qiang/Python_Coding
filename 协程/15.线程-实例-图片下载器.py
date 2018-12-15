
import threading
import urllib.request


def download(img_name, img_url):
   req = urllib.request.urlopen(img_url)
   data = req.read()
   with open(img_name, 'wb') as f:
       f.write(data)


def main():

    t1 = threading.Thread(target=download, args=('5.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/13/1931736_20181113121805_small.jpg"))
    t2 = threading.Thread(target=download, args=('6.jpg', "https://rpic.douyucdn.cn/asrpic/181215/910907_796449_49c50_2_2249.jpg"))

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()





