

def inputMatrix():
    n = int(input("Nhập giá trị n: "))
    m = int(input("Nhập giá trị m: "))

    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            n = input("Nhập giá trị cho matrix: ")
            row.append(n)
        matrix.append(row)
    return matrix

def sumMatrixs(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(int(matrix_a[i][j]) + int(matrix_b[i][j]))
        result.append(row)
    return result
            
print("Matrix A")
matrix_a = inputMatrix()
print(matrix_a)

print("Matrix B")
matrix_b = inputMatrix()
print(matrix_b)

sum_matrix = sumMatrixs(matrix_a, matrix_b)
print("Tổng matrix A và B", sum_matrix)