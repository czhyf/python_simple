
#最高分数
MAX_SCORE=100
#最低分数
MIN_SCORE=0
#初始化分数
INITIAL_SCORE=10
#redi_ip
REDIS_HOST='localhost'
#redis端口
REDIS_PORT=6379
#密码
REDIS_PASSWORD=None
#key
REDIS_KEY='proxies'

import redis
from random import choice



class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        :param host: 主机名
        :param port: 端口号
        :param password: 密码
        """
        self.db=redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        """
        添加代理，设置分数
        :param proxy: 代理
        :param score: 分数
        :return:
        """
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)
    def rendom(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取
        :return:
        """
        result = self.db.zrevrange(REDIS_KEY,0,100)
        if len(result):
            return choice(result)
        else:
            result=self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                pass
    def decrease(self,proxy):
        """
        代理值减少一分，分数小于最小值，则代理删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score=self.db.zscore(REDIS_KEY,proxy)
        if score and score>MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减一')
            return self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY,proxy)
    def exists(self,proxy):
        """
        判断是否存在
        :param proxy:代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY,proxy)==None
    def max(self,proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结束
        """
        print('代理',proxy,'可用，设置为',MAX_SCORE)
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)
    def count(self):
        """
        获取数量
        :return:数量
        """
        return self.db.zcard(REDIS_KEY)
    def all(self):
        """
        获取去哪不代理
        :return:
        """
        return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)