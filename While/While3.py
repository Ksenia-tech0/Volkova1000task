try:
    n = int(input("Введите N: "))
    k = int(input("Введите K: "))
    w = 0
    while n >= k:
        n -= k
        w += 1
    print(f"Частное: {w}")
    print(f"Остаток: {n}")
except ValueError:
    print("Ошибка ввода")