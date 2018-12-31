import requests
from bs4 import BeautifulSoup
import re
from urllib import request
import os
from tqdm import tqdm
'''
    需要安装的lib: [requests,bs4,lxml,tqdm]   否则无法使用 
'''
#得到img的url列表
def get_img_url():
    #定义url列表
    img_list=[]
    start=5001
    for i in range(588):
        page=start+i
        #进行url拼接
        url='http://www.meizitu.com/a/'+str(page)+'.html'
        img_list.append(url)
    return  img_list


#对每一个url进行下载
def dowload(save_path_dir,img_list,header):
    for img in img_list:
        real_dowload_url(save_path_dir,img,header)

#对每一个url进行下载:
def real_dowload_url(save_path,url,header):
    #拿到每一章文件夹的名字
    soup=BeautifulSoup(requests.get(url).text.encode("ISO-8859-1").decode("gbk"),'lxml',header)
    #拿到文件夹的名字
    name=re.match(r'.*l">(.*)</a.*',str(soup.find_all('h2')[1]))

    try:
        #创建文件夹需要改进，可以判断这个文件夹是否存在,存在怎么样，不存在创建等等....
        if os.path.exists(save_path):
            #路径后面是否以/结尾，如果是 则直接进行拼接，如果不是，则加上
            if save_path.endswith("/"):
                # 进行文件夹的拼接
                save_path = save_path + name.group(1)
                img_real_dowload(save_path,soup)
            else:
                #路径没有以"/"结尾，拼接的时候加上
                save_path=save_path+'/'+name.group(1)
                img_real_dowload(save_path,soup)
        else:
            print("此路径不存在，正在创建。。。")
            os.mkdir(save_path)
            # 路径后面是否以/结尾，如果是 则直接进行拼接，如果不是，则加上
            if save_path.endswith("/"):
                # 进行文件夹的拼接
                save_path = save_path + name.group(1)
                img_real_dowload(save_path, soup)
            else:
                # 路径没有以"/"结尾，拼接的时候加上
                save_path = save_path + '/' + name.group(1)
                img_real_dowload(save_path, soup)
    except Exception as e:
        print("--------------发生异常了-------------")
        pass
#对每张图片进行下载
def img_real_dowload(save_path,soup):
    os.mkdir(save_path)
    # 拿到图片集合的
    img_url_list = soup.find_all('img')
    # 定义图片序号
    img_index = 1
    # 通过每一个img标签，通过正则拿到href中的img_url
    for i in tqdm(range(len(img_url_list))):
        # 正则提取   <im.*第.*张.*src="(.*)"/>
        img_url_real = re.match(r'<im.*第.*张.*src="(.*)"/>', str(img_url_list[i]))
        if img_url_real:
            # 拼接图片的保存地址
            img_save_path = save_path + "/" + str(img_index) + '.jpg'
            # 下载图片
            request.urlretrieve(img_url_real.group(1), img_save_path)
            # 图片序号改变
            img_index += 1


#执行方法--修改保存路径便可以使用
def start():
    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'cookie': 'shbid=4419; rur=PRN; mcd=3; mid=W1E7cAALAAES6GY5Dyuvmzfbywic; csrftoken=uVspLzRYlxjToqSoTlf09JVaA9thPkD0; urlgen="{\"time\": 1532050288\054 \"2001:da8:e000:1618:e4b8:8a3d:8932:2621\": 23910\054 \"2001:da8:e000:1618:6c15:ccda:34b8:5dc8\": 23910}:1fgVTv:SfLAhpEZmvEcJn0037FXFMLJr0Y"',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    path=input("请输入图片保存的路径的目录！\n")
    #保存路径
    save_path=path
    dowload(save_path,get_img_url(),header)



if __name__ == '__main__':
    start()
