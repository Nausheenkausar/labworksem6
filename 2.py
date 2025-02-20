import math

def gcd(a, b):
    return math.gcd(a, b)  # Using built-in function

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
