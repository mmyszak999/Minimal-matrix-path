from random import randint
import numpy
import os

cur = os.path.dirname(__file__)
file_path = os.path.relpath('scripts\\file.txt')


class Matrix:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.matrix = []

    def __del__(self):
        pass

    def display_matrix(self):
        print(self.matrix)

    def check_dimensions(self):
        self.matrix = numpy.array(self.matrix)
        if self.x < 2 or self.y < 2:
            raise Exception("\nMatrix has to have 2 columns or 2 rows at least!\n")
        if self.x != self.matrix.shape[0] or self.y != self.matrix.shape[1]:
            raise Exception("\nReal dimensions differ from typed/current dimensions!\n")
        return True

    def set_dimensions(self):
        y = int(input("\nSet the amount of columns:\n"))
        x = int(input("\nSet the amount of rows:\n"))
        self.x, self.y = x, y
        self.check_dimensions()

    def draw_matrix(self):
        self.set_dimensions()
        temp = numpy.matrix([[randint(0, 9) for a in range(self.y)] for b in range(self.x)])
        self.matrix = temp
        return self.matrix

    def correct_dimensions(self, path=file_path, mat_from_file=True):
        if mat_from_file is False:
            self.matrix = numpy.array(self.matrix)
            self.y, self.x = self.matrix.shape[1], self.matrix.shape[0]
            self.check_dimensions()
        else:
            file = open(path)
            row = file.readline().split(" ")
            self.y = len(row)
            self.x = sum(1 for line in file) + 1
            self.check_dimensions()
            file.close()
        return True

    def load_matrix(self, path=file_path):
        self.correct_dimensions(path=path)
        file = open(path)
        for i in range(int(self.x)):
            row = file.readline().split(" ")
            temp = []
            for el in row:
                temp.append(int(el))
            self.matrix += [temp]
        self.matrix = numpy.array(self.matrix)
        file.close()
        return self.matrix