def is_perfect_number(n):
    """Function to check if a number is a perfect number."""
    if n < 2:
        return False  
    
    divisor_sum = 0  # Initialize the sum of divisors

    for i in range(1, n // 2 + 1):  # Loop through potential divisors
        if n % i == 0:  # If 'i' is a divisor of 'n'
            divisor_sum += i  # Add it to the sum

    # A perfect number is equal to the sum of its proper divisors
    return divisor_sum == n  

# Example usage
num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
