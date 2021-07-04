n = 0
k = 0

while True:
    print("Nhap n =")
    user_input_n = input()
    print("Nhap k =")
    user_input_k = input()
    try:
        n = int(user_input_n)
        k = int(user_input_k)
        if n > 0 and k > 0:
            break
    except ValueError:
        pass


def calPermute(n):
    print(n)
    if n == 0:
        return 1
    return calPermute(n-1) * calPermute(n-2)


def calculateComb(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return calculateComb(k-1, n-1) + calculateComb(k, n-1)


print("Hoán vị", calPermute(n))
# print("Tổ hợp =", calculateComb(n=n, k=k))
