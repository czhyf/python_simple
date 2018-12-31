# 淘宝登陆和买东西
from selenium import webdriver
import os
from configparser import ConfigParser
import codecs
import argparse
from splinter.browser import Browser
import time
class hackTaobao(object):
    def readConfig(self,config="config.ini"):
        print("正在配置淘宝配置文件")
        #拿到文件的决定路径。
        path=os.path.join(os.getcwd(),config)
        cp = ConfigParser()
        try:
            cp.readfp(codecs.open(config,'r',"utf-8-sig"))
        except IOError as e:
            print(u'打开配置文件"%s"失败, 请先创建或者拷贝一份配置文件config.ini' % (config))
            input('Press any key to continue')
        #登录名
        self.username=cp.get('login',"username")
        #密码
        self.password=cp.get("login","password")
        #拿到登陆url
        self.logurl=cp.get("urlInfo","login_url")
        #拿到购买url
        self.by_url=cp.get("urlInfo","by_url")
        #拿到浏览器名称
        self.driver_name=cp.get("pathInfo","driver_name")
        #拿到浏览器驱动的路径
        self.executable_path=cp.get("pathInfo","executable_path")
    #进行配置文件的读取
    def load_config(self):
        parser=argparse.ArgumentParser()
        parser.add_argument('-c','--config',help='Specify config file, use absolute path')
        args=parser.parse_args()
        if args.config:
            #使用指定配置文件
            self.readConfig(args.config)
        else:
            self.readConfig()
    #初始化
    def __init__(self):
        self.load_config()
    #登陆界面
    def login(self):
        print("正在登陆中......")
        print(self.logurl)
        self.driver.visit(self.logurl)
        # #打开用户名登陆
        # self.driver.find_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
        # #得到用户名和密码自动填充
        # self.driver.fill("TPL_username",self.username)
        # self.driver.fill("TPL_password",self.password)
        while True:
            if self.driver.url != self.by_url:
                time.sleep(1)
            else:
                break

        #自动登陆
        # self.driver.find_by_xpath('//*[@id="J_SubmitStatic"]').click()
    #拿到验证码
    def get_screenshost(self):
        #获取网页截图
        screen = self.driver
    #入口函数
    def start(self):
        print(self.driver_name+"--"+self.executable_path)
        # 初始化驱动
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        # 初始化浏览器窗口大小
        self.driver.driver.set_window_size(1400, 1000)
        # 登录，自动填充用户名、密码，自旋等待输入验证码，输入完验证码，点登录后，访问 tick_url（余票查询页面）
        self.login()
        self.driver.visit(self.by_url)

if __name__ == '__main__':
    hackTaobao  =  hackTaobao()
    hackTaobao.start()


