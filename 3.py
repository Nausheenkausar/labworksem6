import math

def are_relatively_prime(a, b):
    return math.gcd(a, b) == 1  # If GCD is 1, numbers are relatively prime

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if are_relatively_prime(num1, num2):
    print(f"{num1} and {num2} are relatively prime.")
else:
    print(f"{num1} and {num2} are not relatively prime.")
