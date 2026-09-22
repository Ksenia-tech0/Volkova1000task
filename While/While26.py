try:
    n = int(input("Введите N (>1): "))
    f1 = 1
    f2 = 1
    while f2 < n:
        f1, f2 = f2, f1 + f2
    print(f"F(K-1) = {f1}")
    print(f"F(K+1) = {f1 + f2}")
except ValueError:
    print("Ошибка ввода")