try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a >= b:
        print("Ошибка: A < B")
    else:
        count = 1
        for i in range(a, b + 1):
            for _ in range(count):
                print(i, end=" ")
            print()
            count += 1
except ValueError:
    print("Ошибка ввода")