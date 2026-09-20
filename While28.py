try:
    eps = float(input("Введите eps (>0): "))
    a = 2
    k = 1
    while True:
        prev = a
        a = 2 + 1 / a
        k += 1
        if abs(a - prev) < eps:
            break
    print(f"K = {k}, A(K-1) = {prev}, A(K) = {a}")
except ValueError:
    print("Ошибка ввода")