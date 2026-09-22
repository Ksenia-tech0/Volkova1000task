import math
try:
    n = int(input("Введите N (>1): "))
    a = float(input("Введите A: "))
    b = float(input("Введите B: "))
    h = (b - a) / n
    print(f"H = {h}")
    for i in range(n + 1):
        x = a + i * h
        f = 1 - math.sin(x)
        print(f"F({x}) = {f}")
except ValueError:
    print("Ошибка ввода")