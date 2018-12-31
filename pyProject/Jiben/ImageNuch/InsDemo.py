#通过一个页面拿到所有有用的url
#拿到所有的<a>标签 得到 hrf
from ImageNuch import InsImage
from selenium import webdriver


if __name__ == '__main__':
    print(1)
    dirverPath='/Users/caozhan/project/pyProject/angry/chromedriver'
    driver = webdriver.Chrome(dirverPath)
    # target = "https://www.instagram.com/mirei_kiritani_/"
    # target = 'https://www.instagram.com/kasumi_arimura.official/'
    target = 'http://www.veryins.com/tag/%E4%BF%9D%E6%97%B6%E6%8D%B7911'
    url_set = set([])

    driver.get(target)

    url_set_size = 0

    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'cookie': 'shbid=4419; rur=PRN; mcd=3; mid=W1E7cAALAAES6GY5Dyuvmzfbywic; csrftoken=uVspLzRYlxjToqSoTlf09JVaA9thPkD0; urlgen="{\"time\": 1532050288\054 \"2001:da8:e000:1618:e4b8:8a3d:8932:2621\": 23910\054 \"2001:da8:e000:1618:6c15:ccda:34b8:5dc8\": 23910}:1fgVTv:SfLAhpEZmvEcJn0037FXFMLJr0Y"',
        'referer': 'https://www.instagram.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }


    divs = driver.find_elements_by_class_name('caption ')
    for u in divs:
        try:
            real_url = u.find_element_by_tag_name("a").get_attribute('href')
            # conti
            url_set.add(real_url)
            # print("Number of urls is now:" + str(url_set_size))
            if len(url_set) == len(divs):
                break
            url_set_size = len(url_set)
            print(url_set)
        except Exception:
            continue

    url_set_size = len(url_set)

    print("Starting download............")
    i = 0;

    for ind,url_ in enumerate(url_set):
        url=str(url_)
        len=InsImage.xiazai(url,i)
        i=i+len


