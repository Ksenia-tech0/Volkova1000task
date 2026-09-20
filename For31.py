try:
    n = int(input("Введите N (>0): "))
    a = 2
    for i in range(1, n + 1):
        a = 2 + 1 / a
        print(f"A{i} = {a}")
except ValueError:
    print("Ошибка ввода")