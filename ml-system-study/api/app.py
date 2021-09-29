from flask import Flask
from flask import jsonify
from flask import request

import numpy as np
import yfinance as yf
import uuid

from model import MeanModel
from cache import RedisCache
from logger import LogService


logger = LogService("API")
app = Flask(__name__)
logger.log("Created Flask app")
model = MeanModel()
logger.log("Initialized {}".format(model.name()))
cache = RedisCache()
id = str(uuid.uuid4())
logger.log("Assigned id {} to server".format(id))

@app.route("/predict/<ticker_id>")
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
            prediction = model.predict_next(data)
            logger.log("Generated prediction with {}".format(model.name()))
            response = {
                "prediction": prediction,
                "server_id": id
            }
            cache.set(ticker_id, prediction)
            return response
        else:
            logger.log("Failed to predict {}".format(ticker_id))
            return "Ticker ID {} not available".format(ticker_id), 400

@app.route("/log/")
def show_log():
    try:
        count = int(request.args.get('count'))
    except:
        count = 50
    log = logger.read_log()
    result = list(reversed(log[len(log) - count: len(log)]))
    return jsonify(result)

def _fetch_historical_data(ticker_id):
    logger.log("Requested historical data for {}".format(ticker_id))
    try:
        ticker = yf.Ticker(ticker_id)
        data = ticker.history(period="1d", interval="1h")
        return data["Open"].to_numpy()
    except:
        logger.log("Failed to fetch historical data for {}".format(ticker_id))
        return np.array([])
