print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))

x_difference = x1 - x2

y_difference = y1 - y2

if x_difference == 0:
    x_difference = x1

k = y_difference / x_difference

b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки: ")

print("y = ", k, " * x + ", b)
