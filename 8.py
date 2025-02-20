def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(num // 2) + 1):  # Loop up to sqrt(num)
        if num % i == 0:
            return False  # If divisible, it's not prime
    
    return True  # If no divisors, it's prime

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
