import itchat
import time
print("扫描弹出的微信")
b = input("你要发给谁")
itchat.auto_login()
users=itchat.search_friends(name=b)
print(users)
username=users[0]['UserName']
i=0
while True:
    a = str(i)
    time.sleep(0.1)
    itchat.send(a,toUserName=username)
    i=i+1