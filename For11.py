N = int(input("Введите целое число"))
sum = 0
for i in range(N, 2 * N + 1):
    sum += i ** 2
print(f"Сумма квадратов от {N}**2 до (2*{N})**2 = {sum}")