A = float(input("Введите число"))
B = float(input("Введите число"))
C = float(input("Введите число"))
D = B**2 - 4 * A * C
x1 = (-B + (D ** 0.5)) / (2 * A)
x2 = (-B - (D ** 0.5)) / (2 * A)
print(f"x1 = {x1}, x2 = {x2}")
print(f"x1 = {x2}, x2 = {x1}")