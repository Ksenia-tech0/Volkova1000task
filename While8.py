try:
    n = int(input("Введите N: "))
    k = 0
    while (k + 1) ** 2 <= n:
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")