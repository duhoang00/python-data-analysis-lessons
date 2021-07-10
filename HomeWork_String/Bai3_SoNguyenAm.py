s = input("Nhập chuỗi: ")

arr = s.split("-")


for words in arr:
    number = ""
    for word in words:
        try:
            n = int(word)
            number += word
        except ValueError:
            break
    if number != "":
        print("-"+number)
