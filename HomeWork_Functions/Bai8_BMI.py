w = 0
h = 0

while True:
    user_input_w = input("Nhập cân nặng (kg) = ")
    user_input_h = input("Nhập chiều cao (m) = ")
    try:
        w = float(user_input_w)
        h = float(user_input_h)
        if w > 0 and h > 0:
            break
    except ValueError:
        pass

def calBMI(w, h):
    bmi = w / (h * h)
    print("BMI =",bmi)
    if bmi < 18.5:
        return "Gầy"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Mập"
    else:
        return "Béo phì"

print(calBMI(w=w, h=h))