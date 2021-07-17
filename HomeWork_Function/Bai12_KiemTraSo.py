n = 0

while True:
    user_input = input("Nhập N = ")
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass


def printNumberType(n):
    sum = 0
    for index in range (1, n):
        if n % index == 0:
            sum += index
    if sum == n:
        print(n,"là số hoàn thiện")
    elif sum > n:
        print(n,"là số thịnh vượng")
    else:
        print(n,"không phải là số hoàn thiện hay thịnh vượng")


printNumberType(n = n)