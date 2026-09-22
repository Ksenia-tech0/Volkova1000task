try:
    n = int(input("Введите N (>1): "))
    f1 = 1
    f2 = 1
    print(f"F1 = {f1}")
    if n >= 2:
        print(f"F2 = {f2}")
    for i in range(3, n + 1):
        f3 = f1 + f2
        print(f"F{i} = {f3}")
        f1 = f2
        f2 = f3
except ValueError:
    print("Ошибка ввода")