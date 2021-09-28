from .base_model import BaseModel
import numpy as np


# The simplest model to predict future price
# Outputs the average of input data
class MeanModel(BaseModel):

    def __init__(self, logger = None):
        self.logger = logger
        if self.logger is not None:
            self.logger.log("Initialized mean model")

    def predict_next(self, x):
        x = np.array(x)
        if len(x.shape) > 1:
            raise ValueError("Input should be one-dimensional array, got shape {} instead".format(x.shape))
        if self.logger is not None:
            self.logger.log("Generated prediction with mean model")
        return np.mean(x)

    def train(self, data):
        pass
