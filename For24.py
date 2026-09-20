try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    g = 1
    e = 1
    for i in range(1, n + 1):
        e *= -x * x / ((2 * i - 1) * (2 * i))
        g += e
    print(g)
except ValueError:
    print("Ошибка ввода")