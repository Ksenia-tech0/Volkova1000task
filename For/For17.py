A = float(input("Введите число"))
N = int(input("Введите число"))
sum = 1
a = 1
for i in range(1, N + 1):
    a *= A
    sum += a
print(f"Сумма {sum}")