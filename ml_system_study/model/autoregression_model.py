from .base_model import BaseModel
from statsmodels.tsa.ar_model import AutoReg
import numpy as np


class AutoregressionModel(BaseModel):

    def __init__(self, lag):
        self.lag = lag
        self.model = None

    def name(self):
        return "autoregression model"

    def predict_next(self, x):
        if x.shape[0] < self.lag:
            raise ValueError("Length of the model input is smaller than the lag value")
        if self.model is None:
            raise ValueError("Called predict but the model is not yet initialized")
        # x[:-n-1:-1] returns n last elements of x in reversed order
        return sum(self.model.params *
                   np.concatenate((np.array([1]), x[:-(1 + self.lag):-1])))

    def train(self, data):
        self.model = AutoReg(data, lags=self.lag).fit()
