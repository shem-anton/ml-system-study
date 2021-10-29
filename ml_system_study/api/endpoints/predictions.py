
from services import StockPredictionService
from clients import redis
from fastapi import APIRouter

router = APIRouter()

@router.get("/log/")
async def show_log(count: int = 50):
    result = model.hallo
    model.test()
    return result

@router.get("/log2/")
async def show_log(count: int = 50):
    result = model.hallo
    model.test()
    return result
# @app.get("/predict/{ticker_id}")
# async def serve_prediction(ticker_id):
#     logger.log("API is queried for prediction on {}".format(ticker_id))
#     if cache.contains(ticker_id):
#         prediction = cache.get(ticker_id)
#         response = {
#                 "prediction": prediction,
#                 "server_id": id
#             }
#         logger.log("Returning prediction from cache")
#         return response
#     else:        
#         data = _fetch_historical_data(ticker_id)
#         if data.shape[0] > 0:
#             prediction = active_model.predict_next(data)
#             logger.log("Generated prediction with {}".format(active_model.name()))
#             response = {
#                 "prediction": prediction,
#                 "server_id": id
#             }
#             cache.set(ticker_id, prediction)
#             return response
#         else:
#             logger.log("Failed to predict {}".format(ticker_id))
#             raise HTTPException(status_code=400, detail="Ticker ID {} not available".format(ticker_id))

# @app.get("/log/")
# async def show_log(count: int = 50):
#     log = logger.read_log()
#     result = list(reversed(log[len(log) - count: len(log)]))
#     return result

# @app.post("/model/")
# async def update_model(model: Model):
#     try:
#         logger.log("Requested switching to {}".format(model.name))
#         active_model = ModelLoader.create(model.name, model.parameters)
#     except ValueError:
#         logger.log("Unable to create {}".format(model.name))
#         raise HTTPException(status_code=400, detail="Wrong model name {}".format(model.name))

# def _fetch_historical_data(ticker_id):
#     logger.log("Requested historical data for {}".format(ticker_id))
#     try:
#         ticker = yf.Ticker(ticker_id)
#         data = ticker.history(period="1d", interval="1h")
#         return data["Open"].to_numpy()
#     except:
#         logger.log("Failed to fetch historical data for {}".format(ticker_id))
#         return np.array([])
