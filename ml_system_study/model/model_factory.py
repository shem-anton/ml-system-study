import numpy as np

from . import MeanModel
from . import MovingAverageModel
from . import AutoregressionModel


# Trainable models are trained on random data so far
class ModelLoader():

    @staticmethod
    def create(name, *args):
        if name == "mean":
            return MeanModel()
        if name == "moving average":
            # If order is not provided, default to 3
            if len(args) > 0:
                order = args[0]
            else:
                order = 3
            model = MovingAverageModel(order)
            model.train(np.random.rand(20))
            return model
        if name == "autoregression":
            # If lag is not provided, default to 3
            if len(args) > 0:
                lag = args[0]
            else:
                lag = 3
            model = AutoregressionModel(lag)
            model.train(np.random.rand(20))
            return model
        raise ValueError("Model name was not recognized. Select one from [mean, autoregression, moving average]")