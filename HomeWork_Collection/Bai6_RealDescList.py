list_length = int(input("Nhập độ dài list của bạn: "))

list = []
while len(list) < list_length:
    n = input("Nhập giá trị thực vào list: ")
    list.append(float(n))

list.sort(reverse=True)

print(list)