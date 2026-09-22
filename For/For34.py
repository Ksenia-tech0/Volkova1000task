try:
    n = int(input("Введите N (>1): "))
    a1 = 1
    a2 = 2
    print(f"A1 = {a1}")
    if n >= 2:
        print(f"A2 = {a2}")
    for i in range(3, n + 1):
        a3 = (a1 + 2 * a2) / 3
        print(f"A{i} = {a3}")
        a1 = a2
        a2 = a3
except ValueError:
    print("Ошибка ввода")