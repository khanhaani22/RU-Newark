import math

def areaCircle(radius):
    area = math.pi * radius ** 2
    return area

def circumCircle(radius):
    circumference = 2 * math.pi * radius
    return circumference

def areaRect(length, width):
    area = length * width
    return area

def periRect(length, width):
    perimeter = (2 * length) + (2 * width)
    return perimeter 