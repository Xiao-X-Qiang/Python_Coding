import re

a = "上映日期: 2019-03-02(中国大陆)"


b = re.search(r"上映日期: (\d+?)-\d",a).group(1)
print(b)