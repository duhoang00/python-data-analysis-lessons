email = input("Nhập chuỗi: ")


def validate(email):
    validated_email = ""
    for c in email:
        print(c)
        if c.isdigit() == False or c.isaplpha() == False and c != "@" and c != ".":
            return False, validated_email
        else:
            validated_email += c
    return True, validated_email


validate_email_result, validated_email = validate(email)


if validate_email_result == True:
    arr = validated_email.split("@")

    print("username:", arr[0], " domain_name:", arr[1])
else:
    print("Email không hợp lệ")
