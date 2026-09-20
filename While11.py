try:
    n = int(input("Введите N: "))
    k = 0
    m = 0
    while m < n:
        k += 1
        m += k
    print(f"K = {k}, сумма = {m}")
except ValueError:
    print("Ошибка ввода")