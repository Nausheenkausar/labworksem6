def is_prime(n):
    if n < 2:
        return False  # Prime numbers are greater than 1
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter an integer: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
