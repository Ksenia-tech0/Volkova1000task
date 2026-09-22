try:
    a = float(input("Введите A: "))
    k = 0
    f = 0
    while f <= a:
        k += 1
        f += 1 / k
    print(f"K = {k}, сумма = {f}")
except ValueError:
    print("Ошибка ввода")