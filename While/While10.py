try:
    n = int(input("Введите N: "))
    k = 0
    x = 1
    while x * 3 < n:
        x *= 3
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")