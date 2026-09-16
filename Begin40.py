A1 = float(input("Введите число"))
B1 = float(input("Введите число"))
C1 = float(input("Введите число"))
A2 = float(input("Введите число"))
B2 = float(input("Введите число"))
C2 = float(input("Введите число"))
D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D
print(f"x {x}, y {y}")