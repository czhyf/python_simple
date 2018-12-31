from lxml import etree
import requests
from bs4 import BeautifulSoup
from urllib import request
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context  #ad
head22={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
save_path='/Users/caozhan/Desktop/img/'
re=requests.get('https://www.douyu.com/g_yz',head22,verify=False).text
soup = BeautifulSoup(re,'lxml')
soup=soup.findAll('img',{'class':'JS_listthumb'})
v=1
for found in soup:
   v+=1
   jpg_link=(found.attrs).get('data-original')
   ap_path=save_path+str(v)+".jpg"
   print("第"+str(v)+"张图片正在下载")
   print(jpg_link)
   request.urlretrieve(jpg_link,ap_path)
   time.sleep(1)

# re=re.text
# re=etree.HTML(re)
# result=re.xpath('//*[@id="live-list-contentbox"]/li[3]/a/span/img')
# print(result)
