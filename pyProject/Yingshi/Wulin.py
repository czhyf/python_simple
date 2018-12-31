import requests
import json
url='http://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid=6e2dceca3232483088e0e5584b121317&tz=-8&from=000tv&url=http://tv.cntv.cn/video/C10881/6e2dceca3232483088e0e5584b121317&idl=32&idlr=32&modifyed=false&tsp=1538912269&vn=1540&vc=B1CC508F18B7B1BE4A04A421D82D179B&uid=308893ECB69483A4151B71720BF1117E'
a=requests.get(url).text
d=json.loads(a)
#有用的价值
e=d['video']
print(e)
print(e['lowChapters'])
lena=e['chapters']
def get_response(url):
    # 为了防止被网站禁止访问，携带浏览器参数，假装浏览器请求
    headers = {        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'    }
    # 取出返回的数据
    response = requests.get(url=url,headers=headers).content
    return response


def save_filr(mave_path,url):
    resp=get_response(url)
    with open(mave_path,'ab') as fp:
        fp.write(resp)
index=1
for i in range(len(lena)):
    save_path = '/Users/caozhan/Desktop/wulin/'+str(index)+'.mp4'
    print("正在下载")
    save_filr(save_path,lena[i]['url'])
    print(lena[i]['url'])
    index+=1

'''
    超清
http://api.xyingyu.com/?url=

超清
http://api.greatchina56.com/?url=

超清

http://jx.618g.com/?url=

http://www.pearvideo.com/category_9
'''


