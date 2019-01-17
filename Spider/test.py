#
import re

dict1 = ["\xa0","\r\n","hello"]

dict = [ re.sub(r"\xa0|\s","",i) for i in dict1]  # 将\xa0或空白字符替换成空字符串

dict = [ i for i in dict if len(i)>0 ]  # 剔除空字符串



print(dict)
print(dict1)

# import re,json
#
# import requests
#
# ret  = requests.get("https://csearch.suning.com/emall/cshop/queryByGroup.do?vendor_Id=0070079390&groupId=244011&start=0&cityId=010&rows=48")
#
# ret  = ret.content.decode()
#
# ret1 = re.search(r"jsonpQueryByGroup\((.*)\)",ret).groups()[0]
#
# ret2 = json.loads(ret1)
#
# print(ret2["totalSize"])
#
#
# # print(ret1)