try:
    n = int(input("Введите N: "))
    while n > 0:
        digit = n % 10
        print(digit)
        n //= 10
except ValueError:
    print("Ошибка ввода")