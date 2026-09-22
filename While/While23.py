try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(f"НОД = {a}")
except ValueError:
    print("Ошибка ввода")