import math


# Function to calculate areas
def calculate_areas(A, B, C):
    # Area of the rectangle triangle
    area_triangle = (A * C) / 2

    # Area of the circle
    area_circle = 3.14159 * (C ** 2)

    # Area of the trapezium
    area_trapezium = ((A + B) * C) / 2

    # Area of the square
    area_square = B ** 2

    # Area of the rectangle
    area_rectangle = A * B

    return area_triangle, area_circle, area_trapezium, area_square, area_rectangle


# Function to format and print results
def print_results(areas):
    messages = ["TRIANGULO:", "CIRCULO:", "TRAPEZIO:", "QUADRADO:", "RETANGULO:"]

    for message, area in zip(messages, areas):
        print(f"{message} {area:.3f}")


# Reading input values
A, B, C = map(float, input().split())

# Calculating areas
areas = calculate_areas(A, B, C)

# Printing results
print_results(areas)
