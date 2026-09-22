N = int(input("Введите число"))
f = 1
sum = 1
for i in range(1, N + 1):
    f *= i
    sum += 1
    print(f"Факториал числа {N} ({N}!) = {f}", f"Сумма {sum}")