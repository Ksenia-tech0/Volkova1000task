try:
    n = int(input("Введите N (>2): "))
    a1 = 1
    a2 = 2
    a3 = 3
    print(f"A1 = {a1}")
    print(f"A2 = {a2}")
    print(f"A3 = {a3}")
    for i in range(4, n + 1):
        a4 = a3 + a2 - 2 * a1
        print(f"A{i} = {a4}")
        a1 = a2
        a2 = a3
        a3 = a4
except ValueError:
    print("Ошибка ввода")