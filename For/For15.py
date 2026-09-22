A = float(input("Введите число"))
N = int(input("Введите число"))
r = 1
for i in range(1, N + 1):
    r *= A
print(f"Число {A} в степени {N} = {r}")