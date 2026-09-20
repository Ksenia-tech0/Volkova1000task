try:
    x = float(input("Введите X: "))
    n = int(input("Введите N: "))
    p = 1
    o = 1
    for i in range(1, n + 1):
        o *= x / i
        p += o
    print(p)
except ValueError:
    print("Ошибка ввода")