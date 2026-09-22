try:
    a = float(input("Введите A: "))
    k = 0
    e = 0
    while e + 1 / (k + 1) < a:
        k += 1
        e += 1 / k
    print(f"K = {k}, сумма = {e}")
except ValueError:
    print("Ошибка ввода")