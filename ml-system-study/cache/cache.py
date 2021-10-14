import redis
# Use importlib to import module with hyphen in name
import importlib
ml_system_study = importlib.import_module("ml-system-study")
LogService = getattr(ml_system_study, 'LogService')


class RedisCache():

    def __init__(self, host, port=6379):
        self.redis = redis.Redis(host=host, port=port)
        self.logger = LogService("Cache")
        self.logger.log("Connected to Redis server")
        
    def contains(self, key):
        self.logger.log("Checked existence of {} in cache".format(key))
        return self.redis.exists(key) == 1
    
    def get(self, key):
        self.logger.log("Accessed key {} in cache".format(key))
        return float(self.redis.get(key))
    
    def set(self, key, value):
        self.logger.log("Added {} to cache".format(key))
        self.redis.set(key, value, ex=300)
