from fastapi import FastAPI
from api.api import api_router

import uuid
import configparser

from model import ModelLoader
from cache import RedisCache
from logger import LogService
from schemas import Model


config = configparser.ConfigParser()
config.read('config.ini')
logger = LogService("API", 
                    config["REDIS"]["HOST"], 
                    config["REDIS"]["PORT"])
app = FastAPI()
logger.log("Created FastAPI app")
cache = RedisCache(LogService("Cache", 
                   config["REDIS"]["HOST"], 
                   config["REDIS"]["PORT"]),
                   config["REDIS"]["HOST"], 
                   config["REDIS"]["PORT"])
id = str(uuid.uuid4())
logger.log("Assigned id {} to server".format(id))

app.include_router(api_router)
