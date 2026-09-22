try:
    n = int(input("Введите N: "))
    while n % 3 == 0 and n > 1:
        n //= 3
    print(n == 1)
except ValueError:
    print("Ошибка ввода")