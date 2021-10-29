from fastapi import FastAPI, HTTPException
from api.api import api_router

import numpy as np
import yfinance as yf
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
logger.log("Created Flask app")
active_model = ModelLoader.create(config["MODEL"]["DEFAULT"])
logger.log("Initialized {}".format(active_model.name()))
cache = RedisCache(LogService("Cache", 
                   config["REDIS"]["HOST"], 
                   config["REDIS"]["PORT"]),
                   config["REDIS"]["HOST"], 
                   config["REDIS"]["PORT"])
id = str(uuid.uuid4())
logger.log("Assigned id {} to server".format(id))


app.include_router(api_router)
