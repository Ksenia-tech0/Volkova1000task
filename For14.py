N = int(input("Введите целое число"))
a = 0
for i in range(1, N + 1):
    a += 2 * i - 1
    print(f"Квадрат числа {i} = {a}")