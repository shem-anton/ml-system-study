from .base_model import BaseModel
import numpy as np


# The simplest model to predict future price
# Outputs the average of input data
class MeanModel(BaseModel):

    def name(self):
        return "mean model"

    def predict_next(self, x):
        x = np.array(x)
        if len(x.shape) > 1:
            raise ValueError("Input should be one-dimensional array, got shape {} instead".format(x.shape))
        return np.mean(x)

    def train(self, data):
        pass
