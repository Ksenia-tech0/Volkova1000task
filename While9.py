try:
    n = int(input("Введите N: "))
    k = 0
    c = 1
    while c <= n:
        c *= 3
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")