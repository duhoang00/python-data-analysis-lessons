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


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)


print("Số hạng thứ",n,"của dãy Fibonacci =",fibo(n=n))