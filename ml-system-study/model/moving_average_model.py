from .base_model import BaseModel
from statsmodels.tsa.statespace.sarimax import SARIMAX


class MovingAverageModel(BaseModel):

    def __init__(self, order):
        self.order = order
        self.model = None

    def name(self):
        return "moving average model"

    def train(self, data):
        self.model = SARIMAX(data, order=(0, 0, self.order)).fit(disp=0)

    def predict_next(self, x):
        if self.model is None:
            raise ValueError("Called predict but the model is not yet initialized")
        if x.shape[0] < self.order:
            raise ValueError("Length of the input is smaller than order of MA model")
        model = SARIMAX(x, order=(0, 0, self.order))
        model = model.smooth(self.model.params)
        return model.forecast()[0]
