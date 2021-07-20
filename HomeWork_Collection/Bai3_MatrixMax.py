import random

n = int(input("Nhập giá trị n: "))
m = int(input("Nhập giá trị m: "))
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(m)]
print(matrix)

r = int(input("Nhập dòng bạn muốn: "))
print(matrix[r-1])

c = int(input("Nhập cột bạn muốn: "))
print([row[c-1] for row in matrix])

max_elem = 0
for row in matrix:
    for elem in row:
        if elem > max_elem:
            max_elem = elem

print ("Phần tử lớn nhất là: ", max_elem)