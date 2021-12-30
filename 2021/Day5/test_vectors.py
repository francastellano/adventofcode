import util.DataLoader
import util.UtilVector

from util import UtilMatrix
import unittest


class TestingVectors(unittest.TestCase):

    def test_vertical_vector1(self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 0
        vector.to_x = 0

        vector.from_y = 0
        vector.to_y = 1

        results = vector.iterate_vector()

        self.assertTrue(results, {0: {0: True, 1: True}})

    def test_vertical_vector2(self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 0
        vector.to_x = 0

        vector.from_y = 1
        vector.to_y = 0

        results = vector.iterate_vector()

        self.assertTrue(results, {0: {0: True, 1: True}})

    def test_horizontal_vector1(self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 0
        vector.to_x = 1

        vector.from_y = 0
        vector.to_y = 0

        results = vector.iterate_vector()

        self.assertTrue(results, {1: {0: True, 1: True}})

    def test_horizontal_vector2(self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 0
        vector.to_x = 1

        vector.from_y = 0
        vector.to_y = 0

        results = vector.iterate_vector()

        self.assertTrue(results, {1: {0: True, 1: True}})

    def test_oblique1 (self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 5
        vector.from_y = 5

        vector.to_x = 6
        vector.to_y = 6

        results = vector.iterate_vector()

        self.assertTrue(results, {5: {5: True}, 6: {6: True}})

    def test_oblique2 (self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 6
        vector.from_y = 6

        vector.to_x = 5
        vector.to_y = 5

        results = vector.iterate_vector()

        self.assertTrue(results, {5: {5: True}, 6: {6: True}})


    def test_oblique3 (self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 5
        vector.from_y = 6

        vector.to_x = 6
        vector.to_y = 5

        results = vector.iterate_vector()

        self.assertTrue(results, {5: {5: True}, 6: {6: True}})

    def test_oblique4 (self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 6
        vector.from_y = 5

        vector.to_x = 5
        vector.to_y = 6

        results = vector.iterate_vector()

        self.assertTrue(results, {5: {5: True}, 6: {6: True}})

    def test_oblique5 (self):
        vector = util.UtilVector.UtilVector()
        vector.from_x = 6
        vector.from_y = 5

        vector.to_x = 5
        vector.to_y = 6

        results = vector.iterate_vector()

        self.assertTrue(results, {5: {5: True}, 6: {6: True}})


if __name__ == '__main__':
    unittest.main()