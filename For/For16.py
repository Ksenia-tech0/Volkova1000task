A = float(input("Введите число"))
N = int(input("Введите число"))
w = A
for i in range(1, N + 1):
    print(f"{A} в степени {i} = {w}")
    w *= A