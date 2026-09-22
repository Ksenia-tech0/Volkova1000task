try:
    a = int(input("Введите A: "))
    b = int(input("Введите B: "))
    c = int(input("Введите C: "))
    count_a = 0
    count_b = 0
    while a >= c:
        a -= c
        count_a += 1
    while b >= c:
        b -= c
        count_b += 1
    total = 0
    while count_b > 0:
        total += count_a
        count_b -= 1
    print(f"Количество = {total}")
except ValueError:
    print("Ошибка ввода")