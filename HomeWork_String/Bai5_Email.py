email = input("Nhập email: ")


def validate(email):
    for c in email:
        if c.isdigit() == True or c.isalpha() == True or c == "@" or c == ".":
            pass
        else:
            return False
    return True


isValidate = validate(email)


if isValidate == True:
    arr = email.split("@")
    if (len(arr) != 2):
        print("Email thiếu usernam hoặc domain name")
    elif arr[1].find(".") == -1:
        print("Domain name không hợp lệ")
    else:
        print("username:", arr[0], " domain_name:", arr[1])
else:
    print("Email không hợp lệ")
