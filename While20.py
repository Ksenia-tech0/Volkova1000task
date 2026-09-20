try:
    n = int(input("Введите N: "))
    found = False
    while n > 0:
        digit = n % 10
        if digit == 2:
            found = True
        n //= 10
    print(found)
except ValueError:
    print("Ошибка ввода")