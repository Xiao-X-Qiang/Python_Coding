
import re

dict1 = ["\xa0","\r\n","hello"]

dict = [ re.sub(r"\xa0|\s","",i) for i in dict1]  # 将\xa0或空白字符替换成空字符串

dict = [ i for i in dict if len(i)>0 ]  # 剔除空字符串



print(dict)
print(dict1)