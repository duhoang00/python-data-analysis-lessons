n = 0
while True:
    print("Nhap N =")
    user_input = input()
    try:
        n = int(user_input)
        if n > 0:
            break
    except ValueError:
        pass

while_sum = 0
count = 1
while count < n:
    if count % 2 == 0:
        while_sum += count
    count += 1
print(while_sum)

for_sum = 0
for number in range(2, n+1, 2):
    for_sum += number
print(for_sum)
