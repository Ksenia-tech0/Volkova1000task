try:
    n = int(input("Введите N: "))
    k = 0
    while n > 1:
        n //= 2
        k += 1
    print(f"K = {k}")
except ValueError:
    print("Ошибка ввода")