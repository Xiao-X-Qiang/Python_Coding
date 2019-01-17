#
import re

temp =""""bp":'1.99'"""


ret = re.findall(r"\"bp\":'(.*?)'",temp)

print(ret[0])


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