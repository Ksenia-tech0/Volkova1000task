try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    w = x
    q = x
    for i in range(1, n + 1):
        q *= -x * x * (2 * i - 1) / (2 * i + 1)
        w += q
    print(w)
except ValueError:
    print("Ошибка ввода")