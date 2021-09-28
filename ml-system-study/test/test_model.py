from unittest import TestCase
import numpy as np
from model import MeanModel
from model import AutoregressionModel


class UnitTestMeanModel(TestCase):

    # Test the correct model output
    def test_model_predictions(self):
        model = MeanModel()
        self.assertEqual(model.predict_next(np.array([1, 2, 3, 4, 5])), 3.0)
        self.assertEqual(model.predict_next(np.array([0])), 0.0)
        self.assertAlmostEqual(model.predict_next(np.array([300, 300.5, 300.6, 299.8, 299.3, 299])), 299.866666666)

    # Verify model performance when input is list, numpy array of various shapes
    def test_input_format(self):
        model = MeanModel()
        self.assertEqual(model.predict_next([1, 2, 3, 4, 5]), 3.0)
        self.assertRaises(ValueError, model.predict_next, np.array([[1, 2], [3, 4]]))
        self.assertEqual(model.predict_next(np.array([10] * 10000)), 10)

class UnitTestAutoregressionModel(TestCase):

    # Test that the model can not be called before training
    def test_model_not_trained(self):
        model = AutoregressionModel(3)
        self.assertRaises(ValueError, model.predict_next, np.array([1,2,3]))

    # Test that the model does not return predictions if input length is smaller than model lag
    def test_short_input(self):
        model = AutoregressionModel(30)
        model.train(np.arange(1000))
        self.assertRaises(ValueError, model.predict_next, np.array([1,2,3]))

    # Test that the model performs correctly on a trivial linear input
    def test_model_output_trivial(self):
        model = AutoregressionModel(3)
        model.train(np.arange(20))
        self.assertAlmostEqual(model.predict_next(np.array([1,2,3,4])), 5)

    # Test that the model performs correctly
    def test_model_output(self):
        model = AutoregressionModel(3)
        model.train(np.arange(20))
        self.assertAlmostEqual(model.predict_next(np.array([20, 22, 24])), 25.333333333333)
        self.assertAlmostEqual(model.predict_next(np.array([30, 30, 31, 31, 32, 32])), 33)
        self.assertAlmostEqual(model.predict_next(np.array([5, 6, 5, 6, 5])), 6)

    # Test that the model can be retrained
    def test_model_retrain(self):
        model = AutoregressionModel(3)
        model.train(np.arange(20))
        self.assertAlmostEqual(model.predict_next(np.array([1,2,3,4])), 5)
        model.train(-np.arange(20))
        self.assertAlmostEqual(model.predict_next(np.array([1,2,3,4])), 3.66666666)
