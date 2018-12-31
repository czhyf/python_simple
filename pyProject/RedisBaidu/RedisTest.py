import redis

db=redis.StrictRedis(host="localhost",port=6379,password=None,decode_responses=True)
print(db)
d={"123":1}
db.zadd("proxy",{"a":int(2)})


