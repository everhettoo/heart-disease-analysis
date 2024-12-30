from unittest import TestCase
import custom_libs.evaluation_helper as ev


class TestModelAccuracyScore(TestCase):
    def test_register_model_accuracy(self):
        ev.set_accuracy('NB',20)
        ev.set_accuracy('DT', 30)

    def test_get_model_accuracy(self):
        acc = ev.get_accuracies()
        print(acc)

