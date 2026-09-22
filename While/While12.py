try:
    n = int(input("Введите N: "))
    k = 0
    s = 0
    while s + k + 1 <= n:
        k += 1
        s += k
    print(f"K = {k}, сумма = {s}")
except ValueError:
    print("Ошибка ввода")