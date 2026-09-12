def area_triangulo(A, B, C):
    p = (A + B + C) / 2
    area = (p * (p - A) * (p - B) * (p - C)) ** 0.5
    return area

area = area_triangulo(3, 4, 5)
print("Área do triángulo:", area)