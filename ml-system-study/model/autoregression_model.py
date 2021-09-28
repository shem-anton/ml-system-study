from .base_model import BaseModel
from statsmodels.tsa.ar_model import AutoReg
import numpy as np


class AutoregressionModel(BaseModel):

    def __init__(self, lag, logger = None):
        self.logger = logger
        self.lag = lag
        self.model = None
        if self.logger is not None:
            self.logger.log("Initialized autoregression model")

    def predict_next(self, x):
        if x.shape[0] < self.lag:
            raise ValueError("Length of the model input is smaller than the lag value")
        if self.model is not None:
            if self.logger is not None:
                self.logger.log("Generated prediction with autoregression model")
            # x[:-n-1:-1] returns n last elements of x in reversed order
            return sum(self.model.params *
                       np.concatenate((np.array([1]), x[:-(1 + self.lag):-1])))
        else:
            raise ValueError("Called predict but the model is not yet initialized")

    def train(self, data):
        self.model = AutoReg(data, lags=self.lag).fit()
        if self.logger is not None:
            self.logger.log("Trained autoregression model")
