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


def calPermute(n):  # n = n! = 1.2.3. ..P. . (n-1).n
    if n == 0:
        return 1
    return calPermute(n-1) * n


def calCombination(n, k):  # Akn = n!/(n-k)!
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return calPermute(n)//(calPermute(k)*calPermute(n-k))


def calPermutation(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    return calPermute(n)//calPermute(n-k)


print("Hoán vị =", calPermute(n))
print("Tổ hợp =", calCombination(n=n, k=k))
print("Chỉnh hợp=", calPermutation(n=n, k=k))
