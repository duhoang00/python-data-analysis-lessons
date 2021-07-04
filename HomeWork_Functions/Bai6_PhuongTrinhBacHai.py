import math

a = 0
b = 0
c = 0

while True:
    print("Nhập a =")
    user_input_a = input()
    print("Nhập b =")
    user_input_b = input()
    print("Nhập c =")
    user_input_c = input()
    try:
        a = int(user_input_a)
        b = int(user_input_b)
        c = int(user_input_c)
        break
    except ValueError:
        pass


def solveQuadraticEquations(a, b, c):
    if (a == 0):
        if (b == 0):
            print("Phương trình vô nghiệm")
        else:
            print("Phương trình có một nghiệm: x =", + (-c / b))
        return
    delta = b * b - 4 * a * c
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print("Phương trình có 2 nghiệm x1 =", x1, ", x2 =", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("Phương trình có nghiệm kép: x1 = x2 =", x1)
    else:
        print("Phương trình vô nghiệm")


solveQuadraticEquations(a, b, c)
