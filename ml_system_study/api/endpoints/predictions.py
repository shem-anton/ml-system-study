from fastapi import APIRouter, HTTPException

import configparser
import uuid
from time import sleep
from services.logging import LogService
from services.prediction import PredictionService

config = configparser.ConfigParser()
config.read('config.ini')
router = APIRouter()
logger = LogService("API predict",
                    config["REDIS"]["HOST"],
                    config["REDIS"]["PORT"])
prediction_service = PredictionService()
id = str(uuid.uuid4())
logger.log("Assigned id {} to server".format(id))

@router.get("/{ticker_id}")
async def serve_prediction(ticker_id: str, model = "mean"):
    logger.log("API is queried for prediction on {}".format(ticker_id))
    sleep(2)
    prediction = prediction_service.predict(ticker_id, model)
    if prediction is None:
        raise HTTPException(status_code=400, detail=f"Ticker ID {ticker_id} not available")
    response = {
                "prediction": prediction,
                "server_id": id
            }
    return response
