try:
    n = int(input("Введите N: "))
    count = 0
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        count += 1
        n //= 10
    print(f"Количество = {count}, сумма = {total}")
except ValueError:
    print("Ошибка ввода")