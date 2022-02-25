from scripts.path import *
from scripts.matrix import *


print("Let's start!\n")
while True:
    option = int(input("\nPick an option assigned to proper number:\n"
                       "1 - load a matrix from file 'file.txt' (make sure the file is in the same directory\n "
                       "as .py files)"
                       "\n2 - fill the matrix with random digits (from 0 to 9)"
                       "\n3 - quit\n\n"))
    test = Matrix()
    p = Path()
    if option == 1:
        test.load_matrix()
        test.display_matrix()
    if option == 2:
        test.draw_matrix()
        test.display_matrix()
    if option == 3:
        print("Bye!\n")
        quit(0)
    if option == 1 or 2:
        test.modify_field()
    p.set_paths(test)
    p.display_results(test)
    p.results_to_file()
    del test
    del p