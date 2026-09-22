try:
    n = int(input("Введите N (>1): "))
    a = float(input("Введите A: "))
    b = float(input("Введите B: "))
    h = (b - a) / n
    print(f"H = {h}")
    for i in range(n + 1):
        point = a + i * h
        print(point)
except ValueError:
    print("Ошибка ввода")