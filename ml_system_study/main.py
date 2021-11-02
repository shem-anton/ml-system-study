from fastapi import FastAPI
from api.api import api_router
import configparser
from services.logging import LogService


config = configparser.ConfigParser()
config.read('config.ini')
logger = LogService("APP", 
                    config["REDIS"]["HOST"], 
                    config["REDIS"]["PORT"])
app = FastAPI()
logger.log("Created FastAPI app")

app.include_router(api_router)
