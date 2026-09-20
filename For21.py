try:
    n = int(input("Введите N: "))
    s = 1
    f = 1
    for i in range(1, n + 1):
        f *= i
        s += 1 / f
    print(s)
except ValueError:
    print("Ошибка ввода")