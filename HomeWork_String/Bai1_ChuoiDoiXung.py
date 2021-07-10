s = input("Nhập chuỗi: ")


def isDX(s):
    for index in range(int(len(s)/2)):
        if s[index] != s[len(s) - 1 - index]:
            return False
    return True


print(isDX(s))
