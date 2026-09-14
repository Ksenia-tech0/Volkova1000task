N = int(input("Введите целое число"))
sum = 0.0
for i in range(1, N + 1):
    a = 1.0 + (i * 0.1)
    b = (-1) ** (i + 1)
    sum += b * a
print(f"Сумма {N} = {sum}")