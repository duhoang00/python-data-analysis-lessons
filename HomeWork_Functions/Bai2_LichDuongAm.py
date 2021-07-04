n = 0

while True:
    print("Nhập N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass


can_arr = ["Canh", "Tân", "Nhâm", "Quý",
           "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi_arr = ["Thân", "Đậy", "Tuất", "Hợi", "Tí", "Sửu",
           "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]

can = can_arr[n % 10]
chi = chi_arr[n % 12]

print("Năm", n, "->", can, chi)
