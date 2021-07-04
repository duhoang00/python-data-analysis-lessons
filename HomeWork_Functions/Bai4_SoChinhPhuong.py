import math

n = 0

while True:
    print("Nhập N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass


def isSquareNumber(n):
    return n == math.isqrt(n) ** 2


if isSquareNumber(n) == True:
    print(n, "là số chính phương")
else:
    print(n, "không phải số chính phương")
