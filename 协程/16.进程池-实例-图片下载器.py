
import multiprocessing
import urllib.request


def download(img_name, img_url):
   req = urllib.request.urlopen(img_url)
   data = req.read()
   with open(img_name, 'wb') as f:
       f.write(data)


def main():

    pool = multiprocessing.Pool(3)
    img_url_dict = {'7.jpg': "https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/13/1931736_20181113121805_small.jpg",
                    "8.jpg": "https://rpic.douyucdn.cn/asrpic/181215/910907_796449_49c50_2_2249.jpg"}

    for i in img_url_dict:
        pool.apply_async(download, args=(i, img_url_dict[i]))

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()





