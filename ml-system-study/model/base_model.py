from abc import ABC, abstractmethod
import numpy as np


class BaseModel(ABC):

    @abstractmethod
    def predict_next(self, x):
        pass

    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def name(self):
        pass

    # Calculate MSE of the model on a list of (previous observations, next observation) pairs
    def evaluate(self, data):
        true, predicted = [], []
        for case in data:
            true.append(case[1])
            predicted.append(self.predict_next(case[0]))
        return np.linalg.norm(np.array(true) - np.array(predicted))
