from scripts.matrix import *
import termcolor


class Path(Matrix):
    def __init__(self):
        super().__init__()
        self.value = 100000000
        self.results = []

    def __del__(self):
        pass

    def start(self, obj):
        temp = int(input("\nType the row number you want to start a path from:\n"))
        starting_index = temp - 1
        if starting_index < 0 or starting_index > obj.x - 1:
            raise Exception("Row has to be greater than 0 and smaller than row amount!\n")
        return starting_index

    def path_step_info(self, col, row, val, res, f_1, f_2, f_3):
        print(f"Row index: {row} | Column index: {col}\n",
              f"Current fields: {f_1}-{f_2}-{f_3}\n",
              f"Tested path value: {val} and path result: {res}\n",
              f"Current path value: {self.value} and path result: {self.results}\n\n")

    def set_paths(self, obj=Matrix(), row=0, column=0, path_value=0, path_result=None, starting_index=None):
        if path_result is None:
            path_result = []
        obj.matrix = numpy.array(obj.matrix)
        if column == 0:
            if starting_index is None:
                row = self.start(obj)
            else:
                row = starting_index
            path_result += [row]
            path_value += obj.matrix[row, 0]

        column += 1

        a = row - 1
        b = row
        c = row + 1

        if row == 0:
            a = obj.x - 1

        if row == obj.x - 1:
            c = 0

        f1 = obj.matrix[a, column]
        f2 = obj.matrix[b, column]
        f3 = obj.matrix[c, column]

        if column == obj.y - 1:
            print(f"\nLast ({column}) column!\n")
            field_value = min(f1, f2, f3)
            path_value += field_value

            if field_value == f1:
                path_result = path_result + [a]
            elif field_value == f2:
                path_result = path_result + [b]
            elif field_value == f3:
                path_result = path_result + [c]
            else:
                print("Wrong value!\n")

            self.path_step_info(column - 1, row, path_value, path_result, f1, f2, f3)

            if self.value > path_value:
                self.value = path_value
                self.results = path_result
                print(f"New path value : {path_value}\n"
                      f"New path result: {path_result}\n\n")
            return self.value

        path_value = path_value + f1
        path_result = path_result + [a]
        self.path_step_info(column-1, row, path_value, path_result, f1, f2, f3)
        self.set_paths(obj, a, column, path_value, path_result)

        path_value = path_value - f1 + f2
        path_result.pop()
        path_result = path_result + [b]
        self.path_step_info(column-1, row, path_value, path_result, f1, f2, f3)
        self.set_paths(obj, b, column, path_value, path_result)

        path_value = path_value - f2 + f3
        path_result.pop()
        path_result = path_result + [c]
        self.path_step_info(column-1, row, path_value, path_result, f1, f2, f3)
        self.set_paths(obj, c, column, path_value, path_result)

        return True

    def results_to_file(self):
        with open("scripts/results.txt", 'w') as file:
            file.write("Row indexes of the path:\n")
            for el in self.results:
                file.write(f"{str(el)} ")
            file.write(f"\n\nThe path value:\n{self.value}")
            file.close()

    def display_results(self, obj):
        print("Row indexes of the path:")
        print(*self.results)
        print(f"\n\nThe path value:\n{self.value}\n")
        self.visualized_results(obj)

    def visualized_results(self, obj=Matrix()):
        print("That's the result:\n")
        for i in range(obj.x):
            temp_row = ""
            for j in range(obj.y):
                digit = str(obj.matrix[i, j])
                for column in range(0, len(self.results)):
                    if j == column and i == self.results[column]:
                        digit = termcolor.colored(digit, 'red')
                temp_row = temp_row + digit + " "
            print(temp_row)