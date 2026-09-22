try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    r = x
    d = x
    for i in range(1, n + 1):
        d *= -x * x / ((2 * i) * (2 * i + 1))
        r += d  
    print(r)
except ValueError:
    print("Ошибка ввода")