n = 0
while True:
    print("Nhap N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass

print("SQUARE 1")
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print("SQUARE 2")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:
            print("*", end="")
        else:
            if j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()

print("TRIANGLE 1")
for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("TRIANGLE 2")
for i in range(n):
    for j in range(n):
        if i == j or j == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("TRIANGLE 3")
for i in range(n):
    for j in range(n):
        if i + j < n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("TRIANGLE 4")
for i in range(n):
    for j in range(n):
        if i + j == n - 1 or i == 0 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
