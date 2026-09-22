try:
    p = float(input("Введите P (0<P<50): "))
    s = 0
    daily = 10
    k = 0
    while s <= 200:
        s += daily
        daily *= 1 + p / 100
        k += 1
    print(f"K = {k}, S = {s}")
except ValueError:
    print("Ошибка ввода")