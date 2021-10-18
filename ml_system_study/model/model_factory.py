from . import MeanModel
from . import MovingAverageModel
from . import AutoregressionModel


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
            return MovingAverageModel(order)
        if name == "autoregression":
            # If lag is not provided, default to 3
            if len(args) > 0:
                lag = args[0]
            else:
                lag = 3
            return AutoregressionModel(lag)
        raise ValueError("Model name was not recognized. Select one from [mean, autoregression, moving average]")