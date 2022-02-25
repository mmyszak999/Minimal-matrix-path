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
        if self.x < 2 or self.y < 2:
            raise Exception("\nMatrix has to have 2 columns or 2 rows at least!\n")
        return True

    def set_dimensions(self):
        y = int(input("\nSet the amount of columns:\n"))
        x = int(input("\nSet the amount of rows:\n"))
        self.x, self.y = x, y
        self.check_dimensions()

    def draw_matrix(self):
        self.set_dimensions()
        temp = numpy.array([[randint(0, 9) for a in range(self.y)] for b in range(self.x)])
        self.matrix = temp
        return self.matrix

    def modify_field(self):
        self.matrix = numpy.array(self.matrix)
        while True:
            loop = int(input("\nIf you want to modify another field - pick 1\n"
                             "If you want to stop - pick 2\n"))
            if loop == 1:
                n_row = int(input("Type the index of the row you want to modify:\n"))
                n_column = int(input("Type the index of the column you want to modify:\n"))
                print(f"Current field value: {self.matrix[n_row, n_column]}")
                n_value = int(input("Pick new field value:\n"))
                self.matrix[n_row, n_column] = n_value
                self.display_matrix()
            else:
                break

    def correct_dimensions(self, path=file_path, mat_from_file=True):
        if mat_from_file is False:
            self.matrix = numpy.array(self.matrix)
            self.y, self.x = self.matrix.shape[1], self.matrix.shape[0]
            print(self.y, self.x)
            self.check_dimensions()
        if mat_from_file is True:
            file = open(path)
            row = file.readline().split(" ")
            self.y = len(row)
            self.x = sum(1 for line in file) + 1
            self.check_dimensions()
            file.close()
        return True

    def load_matrix(self, path=file_path):
        self.correct_dimensions(path=path, mat_from_file=True)
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