a = 0
b = 0

while True:
    user_input_a = input("Nhập a = ")
    user_input_b = input("Nhập b = ")
    try:
        a = int(user_input_a)
        b = int(user_input_b)
        if a > 0 and b > 0:
            break
    except ValueError:
        pass


def biggestWish(a, b):
    if (b == 0):
        return a
    return biggestWish(b, a % b)


print("Ước chung lớn nhất của", a, "và", b, "=", biggestWish(a, b))
