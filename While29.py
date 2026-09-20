try:
    eps = float(input("Введите eps (>0): "))
    a1 = 1.0
    a2 = 2.0
    k = 2
    while True:
        a3 = (a1 + 2 * a2) / 3
        k += 1
        if abs(a3 - a2) < eps:
            break
        a1, a2 = a2, a3
    print(f"K = {k}, A(K-1) = {a2}, A(K) = {a3}")
except ValueError:
    print("Ошибка ввода")