from flask import Flask
import numpy as np
import yfinance as yf
from model import MeanModel
from cache import RedisCache
import uuid


app = Flask(__name__)
model = MeanModel()
cache = RedisCache()
id = str(uuid.uuid4())

@app.route("/<ticker_id>")
def serve_prediction(ticker_id):
    if cache.contains(ticker_id):
        prediction = cache.get(ticker_id)
        response = {
                "prediction": prediction,
                "server_id": id
            }
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
            return response
        else:
            return "Ticker ID {} not available".format(ticker_id), 400

def _fetch_historical_data(ticker_id):
    try:
        ticker = yf.Ticker(ticker_id)
        data = ticker.history(period="1d", interval="1h")
        return data["Open"].to_numpy()
    except:
        return np.array([])
