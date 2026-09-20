try:
    n = int(input("Введите N (>0): "))
    a = 1
    for i in range(1, n + 1):
        a = (a + 1) / i
        print(f"A{i} = {a}")
except ValueError:
    print("Ошибка ввода")