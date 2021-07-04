n = 0

while True:
    print("Nhap N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 1:
            break
    except ValueError:
        pass


def isPrimeNumber(n):
    for index in range(2, n):
        if n % index == 0:
            return False
    return True


if isPrimeNumber(n) == True:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
