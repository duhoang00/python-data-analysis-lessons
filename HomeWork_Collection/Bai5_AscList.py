list_length = int(input("Nhập độ dài list của bạn: "))

list = []
while len(list) < list_length:
    n = input("Nhập giá trị tăng dần vào list: ")
    if len(list) == 0:
        list.append(n)
    elif n > list[len(list) - 1]:
        list.append(n)
    else:
        print("Không hợp lệ, vui lòng nhập lại!")

print(list)