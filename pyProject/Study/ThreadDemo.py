import time,threading
def lop():
    print("thread %s is running..."%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print("thread %s >>>> %s"%(threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ended."%threading.current_thread().name)
print("thread %s is running ..."%threading.current_thread().name)
t=threading.Thread(target=lop,name='Caozhan')
t1=threading.Thread(target=lop,name='Caozhan1')
t.start()
t1.start()
print("thread %s ended."%threading.current_thread().name)