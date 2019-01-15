from selenium import webdriver
import time
import requests
import urllib.request

from aip import AipOcr

# 本地图片文件的识别没有问题，但网络图片的识别现在仍有问题，有待于进一步完善

class DouBan(object):
    def __init__(self):
        self.client = None
        self.url = "https://www.douban.com/misc/captcha?id=Kz1AFsCYZ3lSJdJ0knZ0QsgB:en&size=s"

    # 获取client
    def get_client(self):
        APP_ID = '15399664'
        API_KEY = 'XzXcHP5Km973kYXSvfrffQ8t'
        SECRET_KEY = 'EmcaNLzHKzMNoTyYFZUjCIFcK6kxR1gG'
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 从图片文件中识别
    def get_content_file(self, file):
        options = {}
        options["language_type"] = "ENG"
        options["probability"] = "true"
        content = self.client.basicGeneral(file, options)
        return content

    # 从网络图片中识别
    def get_content_url(self, url):

        # todo(Xiao_Qiang，一直报错)
        pass

        # options = {}
        # # options["language_type"] = "ENG"
        # # options["probability"] = "true"
        #
        # content = self.client.basicAccurate(url, options)
        # return content

    def save_img(self,url):
        img = urllib.request.urlopen(url)
        data = img.read()
        with open("captcha_net.jpg","wb") as f:
            f.write(data)


    # 读取二进制图片信息
    def img_file(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def run(self):
        self.save_img(self.url)

        self.get_client()  # 生成client实例
        img = self.img_file("captcha_net.jpg")
        content = self.get_content_file(img)
        print(content)
        for i in content.get('words_result'):
            print(i.get('words'))



def main():
    douban = DouBan()
    douban.run()


if __name__ == '__main__':
    main()



# from aip import AipOcr
#
# """ 你的 APP_ID API_KEY SECRET_KEY，上面的图已经展示了如何找自己的这三个信息，只需要复制信息，放进去单引号里面就行，均为字符串 """
# APP_ID = '15399664'
# API_KEY = 'XzXcHP5Km973kYXSvfrffQ8t'
# SECRET_KEY = 'EmcaNLzHKzMNoTyYFZUjCIFcK6kxR1gG'
#
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# i = open(r'captcha.jpeg','rb')
# img = i.read()
# message = client.basicGeneral(img)
# for i in message.get('words_result'):
#     print(i.get('words'))

