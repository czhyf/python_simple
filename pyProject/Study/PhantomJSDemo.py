#通过phantomjs   可以不用打开网页
from selenium import webdriver
br=webdriver.PhantomJS()
br.get('https://www.baidu.com')
print()