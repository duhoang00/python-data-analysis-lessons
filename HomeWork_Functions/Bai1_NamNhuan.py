n = 2021

while True:
    print("Nhap N =")
    user_input = input()
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
