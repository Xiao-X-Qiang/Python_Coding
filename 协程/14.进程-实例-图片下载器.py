
import multiprocessing
import urllib.request

def download(img_name, img_url):
   req = urllib.request.urlopen(img_url)
   data = req.read()
   with open(img_name, 'wb') as f:
       f.write(data)


def main():

    p1 = multiprocessing.Process(target=download, args=('3.jpg', "https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/13/1931736_20181113121805_small.jpg"))
    p2 = multiprocessing.Process(target=download, args=('4.jpg', "https://rpic.douyucdn.cn/asrpic/181215/910907_796449_49c50_2_2249.jpg"))

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()





