A = float(input("Введите число"))
N = int(input("Введите число"))
sum = 1
n = 1
for i in range(1, N + 1):
    n *= -A
    sum += n
print(f"Сумма {sum}")