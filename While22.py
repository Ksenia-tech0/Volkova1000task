try:
    n = int(input("Введите N (>1): "))
    is_prime = True
    s = 2
    while s * s <= n:
        if n % s == 0:
            is_prime = False
        s += 1
    print(is_prime)
except ValueError:
    print("Ошибка ввода")