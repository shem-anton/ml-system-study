from flask import Flask
import numpy as np
import yfinance as yf
from model import MeanModel


app = Flask(__name__)
model = MeanModel()

@app.route("/<ticker_id>")
def serve_prediction(ticker_id):
    data = _fetch_historical_data(ticker_id)
    if data.shape[0] > 0:
        response = {
            "prediction": model.predict(data)
        }
        return response
    else:
        return "Ticker ID {} not available".format(ticker_id), 400

def _fetch_historical_data(ticker_id):
    ticker = yf.Ticker(ticker_id)
    data = ticker.history(period="1d", interval="1h")
    try:
        return data["Open"].to_numpy()
    except:
        return np.array([])
