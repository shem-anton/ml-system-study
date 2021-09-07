from unittest import TestCase
import numpy as np
from model.model import MeanModel


class UnitTestMeanModel(TestCase):

    # Test the correct output
    def test_model_predictions(self):
        model = MeanModel()
        self.assertEqual(model.predict(np.array([1, 2, 3, 4, 5])), 3.0)
        self.assertEqual(model.predict(np.array([0])), 0.0)
        self.assertAlmostEqual(model.predict(np.array([300, 300.5, 300.6, 299.8, 299.3, 299])), 299.866666666)

    # Verify model performance when input is list, numpy array of various shapes
    def test_input_format(self):
        model = MeanModel()
        self.assertEqual(model.predict([1, 2, 3, 4, 5]), 3.0)
        self.assertRaises(ValueError, model.predict, np.array([[1, 2], [3, 4]]))
        self.assertEqual(model.predict(np.array([10] * 10000)), 10)
