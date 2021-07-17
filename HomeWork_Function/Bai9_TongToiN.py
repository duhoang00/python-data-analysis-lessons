n = 1

while True:
    user_input = input("Nhập N = ")
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass

sum = 0
for index in range(n+1):
    sum += index

print(sum)