from redis.client import pairs_to_dict_typed
import yfinance as yf
import configparser
import numpy as np

from model import ModelLoader
from services.logging import LogService
from services.cache import RedisCache


class PredictionService():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.logger = LogService("Prediction service",
                        config["REDIS"]["HOST"],
                        config["REDIS"]["PORT"])
        self.cache = RedisCache(LogService("Cache",
                        config["REDIS"]["HOST"],
                        config["REDIS"]["PORT"]),
                        config["REDIS"]["HOST"],
                        config["REDIS"]["PORT"])
        self.model_names = ["mean", "moving average", "autoregression"]
        self.models = [ModelLoader.create(name) for name in self.model_names]

    def _fetch_historical_data(self, ticker_id):
        self.logger.log("Requested historical data for {}".format(ticker_id))
        try:
            ticker = yf.Ticker(ticker_id)
            data = ticker.history(period="1d", interval="1h")
            return data["Open"].to_numpy()
        except:
            self.logger.log("Failed to fetch historical data for {}".format(ticker_id))
            return np.array([])
    
    def predict(self, ticker_id, model):
        print(model)
        if self.cache.contains(ticker_id):
            self.logger.log("Returning prediction from cache")
            return self.cache.get(ticker_id)
        data = self._fetch_historical_data(ticker_id)
        if data.shape[0] > 0:
            try:
                model = self.models[self.model_names.index(model)]
                prediction = model.predict_next(data)
                self.logger.log(f"Generated prediction with {model.name()}")
                self.cache.set(ticker_id, prediction)
                return prediction
            except ValueError:
                self.logger.log("Failed to predict {}".format(ticker_id))
                return None
