import unittest
import numpy

from scripts.matrix import *
from scripts.path import *
from scripts import *

mat = Matrix()
pat = Path()
dir_path = os.path.dirname(__file__)
path_to_file = os.path.relpath('test_load.txt', dir_path)


class PathTests(unittest.TestCase):
    def test_results_length(self):
        self.assertTrue(len(pat.results) == mat.y)

    def test_results(self):
        mat.matrix = numpy.array([
            [3, 4, 1, 2, 8, 6],
            [6, 1, 8, 2, 7, 4],
            [5, 9, 3, 9, 9, 5],
            [8, 4, 1, 3, 2, 6],
            [3, 7, 2, 8, 6, 4]
        ])
        mat.correct_dimensions(mat_from_file=False)
        pat.set_paths(mat, starting_index=0)
        self.assertEqual(pat.results, [0, 1, 2, 3, 3, 4])


if __name__ == '__main__':
    unittest.main()


