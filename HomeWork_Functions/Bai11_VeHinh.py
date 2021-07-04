n = 4

while True:
    print("Nhập N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass


print("Hình a:")
for i in range(n):
    for j in range (n * 2 - 1):
        if j == 0 or j == n - 1 or j == n * 2 - 2:
            print("*", end = "")
        elif j < n - i  and i <= n:
            print("*", end = "")
        elif j >= n * 2 - 2 - i: 
            print("*", end = "")
        else:
            print(" ", end = "")
    print(" ")

print()
print("Hình b:")
for i in range(n):
    for j in range(n * 2 - 1):
        if j == 0 or j == n - 1 or j == n * 2 - 2:
            print("*", end = "")
        elif i == n - 1 and j < n:
            print("*", end = "")
        elif i == 0 and j >= n:
            print("*", end = "")
        elif i == j:
            print("*", end = "")
        elif j - i == n - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print(" ")