try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a >= b:
        print("Ошибка: A < B")
    else:
        for i in range(a, b + 1):
            for _ in range(i):
                print(i, end=" ")
            print()
except ValueError:
    print("Ошибка ввода")