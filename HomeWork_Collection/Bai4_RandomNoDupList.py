import random

list_length = input("Nhập độ dài list mong muốn của bạn: ")
list_random_range = input("Nhập khoảng giá trị bạn muốn random vào list: ")

list = []
for i in range(0, int(list_length)):
    n = random.randint(0, int(list_random_range))
    if n not in list:    
        list.append(n)

print(list)