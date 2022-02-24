import unittest

from scripts.matrix import *
from scripts import *

mat1 = Matrix()
dir_path = os.path.dirname(__file__)
path_to_file = os.path.relpath('test_load.txt', dir_path)


class MatrixTests(unittest.TestCase):
    def test_dimensions(self):
        mat1.load_matrix(path=path_to_file)
        self.assertTrue(mat1.check_dimensions())

    def test_with_wrong_dimensions(self):
        mat1.x, mat1.y = 1, 1
        mat1.load_matrix(path=path_to_file)
        self.assertTrue(mat1.check_dimensions())


if __name__ == '__main__':
    unittest.main()
