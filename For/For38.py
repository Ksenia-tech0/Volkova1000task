try:
    n = int(input("Введите N (>0): "))
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** (n - i + 1)
    print(f"Сумма = {total_sum}")
except ValueError:
    print("Ошибка ввода")