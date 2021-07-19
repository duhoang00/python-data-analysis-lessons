import random


list_length = input("Nhập độ dài list mong muốn của bạn: ")
list_random_range = input("Nhập khoảng giá trị bạn muốn random vào list: ")
k = input("Nhập giá trị k muốn xóa trong list: ")

list = []
for i in range(0, int(list_length)):
    n = random.randint(0, int(list_random_range))
    list.append(n)


def isSymmetric(l):
    if l == []:
        return True
    for i in range(len(l)):
        if l[i] != l[len(l) - 1 - i]:
            return False
    return True


print("List của bạn với dộ dài", list_length,
      "các giá trị đi từ 0 tới", list_random_range, "là ==> ", list)
no_k_list = [x for x in list if x != k]
print("Sau khi xóa đi các giá trị k =", k,
      "thì list của bạn là ==> ", no_k_list)
if isSymmetric(no_k_list) == True:
    print("List của bạn ==> Đối xứng")
else:
    print("List của bạn ==> Không đối xứng")
