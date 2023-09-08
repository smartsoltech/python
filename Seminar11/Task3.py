class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        
    def __repr__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.data])
    
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
        
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
# Инициализация матриц
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
m3 = Matrix([[1, 1], [1, 1]])
m4 = Matrix([[2, 0], [1, 2]])

# Вывод на печать
print("Matrix m1:")
print(m1)

print("Matrix m2:")
print(m2)

# Сравнение
print("m2 == m3:", m2 == m3)
print("m1 == m2:", m1 == m2)

# Сложение
print("m1 + m2:")
print(m1 + m2)

# Умножение
print("m1 * m4:")
print(m1 * m4)
