A = int(input("Введите a"))
B = int(input("Введите b"))
count = 0
for i in range(B - 1, A, -1):
    print(i)
    count += 1
    print("Колличество", count)