try:
    n = int(input("Введите N: "))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print(f"Число = {rev}")
except ValueError:
    print("Ошибка ввода")