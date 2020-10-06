import os

class Matrix:
    def __init__(self, matrix_line):
        self.matrix_line = matrix_line

    def print_row(self):
        self.rows = [list(map(int, row.split(" "))) for row in self.matrix_line.split("\n")]
    
    def print_column(self):
        rows = [list(map(int, row.split(" "))) for row in self.matrix_line.split("\n")]
        self.columns = [list(i) for i in zip(*rows)]


if __name__ == '__main__':
    matrix_example = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
    matrix_example.print_row()
    print(matrix_example.rows)
    matrix_example.print_column()
    print(matrix_example.columns)
