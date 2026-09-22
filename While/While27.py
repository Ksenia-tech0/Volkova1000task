try:
    n = int(input("Введите N (>1): "))
    f1 = 1
    f2 = 1
    k = 2
    while f2 < n:
        f1, f2 = f2, f1 + f2
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")