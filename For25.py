try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    s = 0.0
    p = 1.0
    for i in range(1, n + 1):
        p *= x
        if i % 2 != 0:
            s += p / i
        else:
            s -= p / i
    print(s)
except ValueError:
    print("Ошибка ввода")