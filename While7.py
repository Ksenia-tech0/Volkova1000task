try:
    n = int(input("Введите N: "))
    k = 1
    while k * k <= n:
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")