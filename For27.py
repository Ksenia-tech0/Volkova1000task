try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    p = x
    k = x
    for i in range(1, n + 1):
        k *= ((2 * i - 1) ** 2 * x * x) / (2 * i * (2 * i + 1))
        p += k
    print(p)
except ValueError:
    print("Ошибка ввода")