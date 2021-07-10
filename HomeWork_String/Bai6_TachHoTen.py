fullName = input("Nhập họ và tên: ").lower()

arr = fullName.split()

try:
    print("Họ:", arr[0].capitalize())
    if len(arr) > 2:
        print("Tên đệm: ", end="")
        for index in range(1, len(arr) - 1):
            print(arr[index].capitalize(), end=" ")
        print()
    print("Tên:", arr[len(arr) - 1].capitalize())
except:
    print("Dữ liệu nhập vào không hợp lệ")
