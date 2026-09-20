try:
    n = int(input("Введите N: "))
    e = 1
    while n > 1:
        e *= n
        n -= 2
    print(f"N!! = {e}")
except ValueError:
    print("Ошибка ввода")