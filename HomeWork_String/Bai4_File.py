s = input("Nhập đường dẫn: ")

file_name = ""


for index in range(len(s) - 1):
    c = s[len(s) - 1 - index]
    if c.isalpha() == True or c == ".":
        file_name += c
    else:
        break


if file_name != "":
    print(file_name[::-1])
