import math

square_side = input("Введите длину стороны квадрата: ")

side_convert = float(square_side)
side_convert2 = int(side_convert)
side = math.ceil(side_convert2)

def square(side):
    result = side * side
    print(f"Площадь квадрата = {result}")

square(side)