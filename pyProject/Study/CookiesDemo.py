import requests
r=requests.get("https://www.zhihu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key+"---"+value)