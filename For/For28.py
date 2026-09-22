try:
    x = float(input("Введите X (|X|<1): "))
    n = int(input("Введите N (>0): "))
    v = 1
    b = 1
    for i in range(1, n + 1):
        if i == 1:
            b *= x / 2
        else:
            b *= -x * (2 * i - 3) / (2 * i)
        v += b
    print(v)
except ValueError:
    print("Ошибка ввода")