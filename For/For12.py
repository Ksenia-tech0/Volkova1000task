N = int(input("Введите целое число"))
b = 1
for i in range(1, N + 1):
    c = 1 + (i * 0.1)
    b *= c
print(f"Произведение {N} =  {b}")
