try:
    n = int(input("Введите N: "))
    k = int(input("Введите K: "))
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** k
    print(f"Сумма = {total_sum}")
except ValueError:
    print("Ошибка ввода")