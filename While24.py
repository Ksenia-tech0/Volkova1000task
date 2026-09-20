try:
    n = int(input("Введите N (>1): "))
    f1 = 1
    f2 = 1
    while f2 < n:
        temp = f1 + f2
        f1 = f2
        f2 = temp
    print(f2 == n)
except ValueError:
    print("Ошибка ввода")