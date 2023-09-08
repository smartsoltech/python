
class InvalidMatrixOperation(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise InvalidMatrixOperation("Matrices must have the same dimensions for addition.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise InvalidMatrixOperation("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                cell = 0
                for k in range(self.cols):
                    cell += self.data[i][k] * other.data[k][j]
                row.append(cell)
            result.append(row)
        return Matrix(result)

class InvalidMatrixOperation(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MatrixWithExceptions(Matrix):  # Наследуемся от предыдущего класса Matrix
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise InvalidMatrixOperation("Matrices must have the same dimensions for addition.")
        return super().__add__(other)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise InvalidMatrixOperation("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        return super().__mul__(other)