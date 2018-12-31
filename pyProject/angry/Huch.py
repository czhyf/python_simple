from selenium import webdriver
import time
from PIL import ImageGrab


if __name__ == '__main__':
    list=["小牛学堂 大数据培训","小牛学堂 智能培训","小牛学堂 包就业","小牛学堂 就业服务","小牛学堂 就业答疑","小牛学堂 人工智能培训"]
    dirverPath = "/Users/caozhan/project/pyProject/angry/chromedriver"
    for key1 in list:
        driver = webdriver.Chrome(dirverPath)
        print(key1)
        driver.get("https://www.baidu.com")
        key=driver.find_element_by_xpath('//*[@id="kw"]')
        key.send_keys(key1)
        button=driver.find_element_by_xpath('//*[@id="su"]')
        button.click()
        time.sleep(3)
        im=ImageGrab.grab()
        im.save('/Users/caozhan/Desktop/'+key1+'.png')
