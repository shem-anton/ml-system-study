from flask import Flask
import numpy as np
import yfinance as yf
from model import MeanModel
from cache import RedisCache
from logger import LogService
import uuid


logger = LogService("API")
app = Flask(__name__)
logger.log("Created Flask app")
model = MeanModel()
cache = RedisCache()
id = str(uuid.uuid4())
logger.log("Assigned id {} to server".format(id))

@app.route("/<ticker_id>")
def serve_prediction(ticker_id):
    logger.log("API is queried for prediction on {}".format(ticker_id))
    if cache.contains(ticker_id):
        prediction = cache.get(ticker_id)
        response = {
                "prediction": prediction,
                "server_id": id
            }
        logger.log("Returning prediction from cache")
        return response
    else:        
        data = _fetch_historical_data(ticker_id)
        if data.shape[0] > 0:
            prediction = model.predict(data)
            response = {
                "prediction": prediction,
                "server_id": id
            }
            cache.set(ticker_id, prediction)
            logger.log("Generated new prediction")
            return response
        else:
            logger.log("Failed to predict {}".format(ticker_id))
            return "Ticker ID {} not available".format(ticker_id), 400

def _fetch_historical_data(ticker_id):
    logger.log("Requested historical data for {}".format(ticker_id))
    try:
        ticker = yf.Ticker(ticker_id)
        data = ticker.history(period="1d", interval="1h")
        return data["Open"].to_numpy()
    except:
        logger.log("Failed to fetch historical data for {}".format(ticker_id))
        return np.array([])
