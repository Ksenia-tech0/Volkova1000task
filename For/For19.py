N = int(input("Введите число"))
f = 1
for i in range(1, N + 1):
    f *= i
print(f"Факториал числа {N} ({N}!) = {f}")