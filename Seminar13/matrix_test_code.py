
from matrix_code import Matrix, InvalidMatrixOperation

def run_matrix_test():
    try:
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 1], [1, 1]])
        m3 = m1 + m2
        print("Matrix addition result:", m3.data)
        
        m4 = Matrix([[1, 2], [3, 4], [5, 6]])
        m3 = m1 + m4
    except InvalidMatrixOperation as e:
        print("Exception caught:", e.message)
