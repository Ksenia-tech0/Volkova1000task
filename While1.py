try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a <= b:
        print("Ошибка: A > B")
    else:
        while a >= b:
            a -= b
        print(f"Длина: {a}")
except ValueError:
    print("Ошибка ввода")