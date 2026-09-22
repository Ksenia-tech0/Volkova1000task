try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    if a <= b:
        print("Ошибка: A > B")
    else:
        count = 0
        while a >= b:
            a -= b
            count += 1
        print(f"Количество: {count}")
except ValueError:
    print("Ошибка ввода")