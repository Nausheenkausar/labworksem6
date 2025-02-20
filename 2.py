import math

def volume_sphere():
    num = float(input("Enter the value of radius: "))
    result = (4/3) * math.pi * num**3
    return result

# Calling the function and printing the result
print(f"Volume of the given sphere is: {volume_sphere()}")


