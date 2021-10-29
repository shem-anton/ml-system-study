

class StocklPredictionService():
    def __init__(self, config, cache, model):
        self._model = model
        self._cache = cache
        self._config = config

    def create_prediction(self):
        logger.log("API is queried for prediction on {}".format(ticker_id))
        # if cache.contains(ticker_id):
        #     prediction = cache.get(ticker_id)
        #     response = {
        #             "prediction": prediction,
        #             "server_id": id
        #         }
        #     logger.log("Returning prediction from cache")
        #     return response
        # else:        
        #     data = _fetch_historical_data(ticker_id)
        #     if data.shape[0] > 0:
        #         prediction = active_model.predict_next(data)
        #         logger.log("Generated prediction with {}".format(active_model.name()))
        #         response = {
        #             "prediction": prediction,
        #             "server_id": id
        #         }
        #         cache.set(ticker_id, prediction)
        #         return response
        #     else:
        #         logger.log("Failed to predict {}".format(ticker_id))
        #         raise HTTPException(status_code=400, detail="Ticker ID {} not available".format(ticker_id))
        return 0.0 
