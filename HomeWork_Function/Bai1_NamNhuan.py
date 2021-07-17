n = 0

while True:
    user_input = input("Nhập N = ")
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass

if n % 100 == 0:
    if n % 400 == 0:
        print(n, "là năm nhuận")
    else:
        print(n, "không phải là năm nhuận")
elif n % 4 == 0:
    print(n, "là năm nhuận")
else:
    print(n, "không phải là năm nhuận")
