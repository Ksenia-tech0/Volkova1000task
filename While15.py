try:
    p = float(input("Введите P: "))
    s = 1000
    t = 0
    while s <= 1100:
        s *= 1 + p / 100
        t += 1
    print(f"K = {t}, S = {s}")
except ValueError:
    print("Ошибка ввода")