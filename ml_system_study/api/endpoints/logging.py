import configparser
from fastapi import APIRouter
from services.logging import LogService


config = configparser.ConfigParser()
config.read('config.ini')
logger = LogService("Log access",
                    config["REDIS"]["HOST"],
                    config["REDIS"]["PORT"])

router = APIRouter()
@router.get("/")
async def show_log(count: int = 50):
    logger.log("Accessed logs")
    log = logger.read_log()
    result = list(reversed(log[len(log) - count: len(log)]))
    return result
