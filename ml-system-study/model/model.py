import numpy as np
from logger import LogService


# The simplest model to predict future price
# Outputs the average of input data
class MeanModel:

    def __init__(self):
        self.logger = LogService("Model")
        self.logger.log("Initialized mean model")

    def predict(self, x):
        x = np.array(x)
        if len(x.shape) > 1:
            raise ValueError("Input should be one-dimensional array, got shape {} instead".format(x.shape))
        self.logger.log("Generated prediction with mean model")
        return np.mean(x)
