import math

def area_circle():
    radius = int(input("Enter radius: "))
    area = math.pi * radius ** 2
    return area

# Calling the function and printing the result
print("Area of the circle:", area_circle())
