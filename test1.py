

import requests
import  json

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0"
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

response = requests.get(url=url,headers=header)

# result = response.content.decode()

result_1 = json.loads(response.content)
print(result_1.get("subjects"))
