s = input("Nhập chuỗi: ")

arr = s.split()

for words in reversed(arr):
    print(words, end=" ")
print()
