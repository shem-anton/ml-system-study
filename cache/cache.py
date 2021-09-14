import redis


class RedisCache():

    def __init__(self):
        self.redis = redis.Redis()
        
    def contains(self, key):
        return self.redis.exists(key) == 1
    
    def get(self, key):
        return float(self.redis.get(key))
    
    def set(self, key, value):
        self.redis.set(key, value, ex=300)
