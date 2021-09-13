from flask import Flask
import numpy as np
import yfinance as yf
from model import MeanModel
import random


app = Flask(__name__)
model = MeanModel()
id = random.random()

@app.route("/<ticker_id>")
def serve_prediction(ticker_id):
    data = _fetch_historical_data(ticker_id)
    if data.shape[0] > 0:
        response = {
            "prediction, id {}".format(id): model.predict(data)
        }
        return response
    else:
        return "Ticker ID {} not available, id {}".format(ticker_id, id), 400

def _fetch_historical_data(ticker_id):
    try:
        ticker = yf.Ticker(ticker_id)
        data = ticker.history(period="1d", interval="1h")
        return data["Open"].to_numpy()
    except:
        return np.array([])
