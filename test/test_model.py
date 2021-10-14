from unittest import TestCase
import numpy as np
# Use importlib to import module with hyphen in name
import importlib
ml_system_study = importlib.import_module("ml-system-study.model")
MeanModel = getattr(ml_system_study, 'MeanModel')
AutoregressionModel = getattr(ml_system_study, 'AutoregressionModel')
MovingAverageModel = getattr(ml_system_study, 'MovingAverageModel')

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

    # Verify model evaluation
    def test_model_evaaluate(self):
        model = MeanModel()
        data = [[np.array([1, 2, 3, 4, 5]), 6],
                [np.array([2, 2, 3, 2, 1]), 6],
                [np.array([1, 1, 1]), 1]]
        self.assertAlmostEqual(model.evaluate(data), 5)

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

    def test_model_evaluate(self):
        model = AutoregressionModel(3)
        model.train(np.arange(20))
        data = [[np.array([1, 2, 3, 4, 5]), 3],
                [np.array([2, 2, 3, 2, 1]), 5.333333333],
                [np.array([7, 7, 8, 7, 7]), 7.333333333]]
        self.assertAlmostEqual(model.evaluate(data), 5)

class UnitTestMovingAverageModel(TestCase):

    # Test that the model can not be called before training
    def test_model_not_trained(self):
        model = MovingAverageModel(3)
        self.assertRaises(ValueError, model.predict_next, np.array([1,2,3]))

    # Test that the model does not return predictions if input length is smaller than model lag
    def test_short_input(self):
        model = MovingAverageModel(30)
        model.train(np.arange(1000))
        self.assertRaises(ValueError, model.predict_next, np.array([1,2,3]))

    # Test that the model outputs a real number in reasonable range
    def test_model_output(self):
        model = MovingAverageModel(2)
        model.train(np.arange(20))
        prediction = model.predict_next(np.array([15, 15, 15, 15]))
        self.assertGreater(prediction, 0)
        self.assertLess(prediction, 20)

    # Test that the model can be retrained
    def test_model_retrain(self):
        model = MovingAverageModel(2)
        model.train(np.arange(20))
        first_prediction = model.predict_next(np.array([20, 22, 24]))
        model.train(np.array([15] * 20))
        self.assertNotAlmostEqual(model.predict_next(np.array([20, 22, 24])), first_prediction)

    # Test model evaluation
    def test_model_evaluate(self):
        model = MovingAverageModel(2)
        model.train(np.arange(20))
        data = [[np.array([20, 22, 24]), 14.438],
                [np.array([15, 15, 15, 15]), 13.238],
                [np.array([5, 6, 5, 6, 5]), 1.309]]
        evaluation = model.evaluate(data)
        self.assertGreater(evaluation, 0)
        self.assertLess(evaluation, 20)
