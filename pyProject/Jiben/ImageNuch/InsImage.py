from urllib import request
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains





def download_img(url,save_path):
    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'cookie': 'shbid=4419; rur=PRN; mcd=3; mid=W1E7cAALAAES6GY5Dyuvmzfbywic; csrftoken=uVspLzRYlxjToqSoTlf09JVaA9thPkD0; urlgen="{\"time\": 1532050288\054 \"2001:da8:e000:1618:e4b8:8a3d:8932:2621\": 23910\054 \"2001:da8:e000:1618:6c15:ccda:34b8:5dc8\": 23910}:1fgVTv:SfLAhpEZmvEcJn0037FXFMLJr0Y"',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    print(url)
    req=request.Request(url=url,headers=header)
    web_img=request.urlopen(req)
    content=web_img.read()
    fp=open(save_path,'wb')
    fp.write(content)
    fp.close()


def xiazai(url_img,i):
    print(0)
    driver = webdriver.Chrome('/Users/caozhan/project/pyProject/angry/chromedriver')
    print(1)
    # target = "https://www.instagram.com/mirei_kiritani_/"
    # target = 'https://www.instagram.com/kasumi_arimura.official/'
    target = url_img
    print(2)
    url_set = set([])

    driver.get(target)

    url_set_size = 0

    save_dir = './pic_test/'

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'cookie': 'shbid=4419; rur=PRN; mcd=3; mid=W1E7cAALAAES6GY5Dyuvmzfbywic; csrftoken=uVspLzRYlxjToqSoTlf09JVaA9thPkD0; urlgen="{\"time\": 1532050288\054 \"2001:da8:e000:1618:e4b8:8a3d:8932:2621\": 23910\054 \"2001:da8:e000:1618:6c15:ccda:34b8:5dc8\": 23910}:1fgVTv:SfLAhpEZmvEcJn0037FXFMLJr0Y"',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    while (True):

        divs = driver.find_elements_by_class_name('img-wrap')
        for u in divs:
            real_url = u.find_element_by_tag_name('img').get_attribute('src')
            url_set.add(real_url)

        print("Number of urls is now:" + str(url_set_size))

        if len(url_set) == url_set_size or len(url_set) > 30:
            break

        url_set_size = len(url_set)

        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        # driver.implicitly_wait(30) #智能等待30秒

    url_set_size = len(url_set)
    j=i
    print("Starting download..........")
    for ind, url_ in enumerate(url_set):
        save_path = '/Users/caozhan/Desktop/img/'+str(j)+'.jpg' #你图片要保存的路径
        download_img(url_,save_path) #
        print(url_ + ' has been downloaded, and the total process finished {:.2f}%'.format(ind / url_set_size * 100))
        j=j+1
        print(j)
    return len(url_set)