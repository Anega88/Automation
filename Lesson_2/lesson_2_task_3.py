import math

square_side = input("Введите длину стороны квадрата: ")

side_convert = float(square_side)

def square(side_convert):
    result = (side_convert * side_convert)
    result = math.ceil(result)
    print(f"Площадь квадрата = {result}")

square(side_convert)