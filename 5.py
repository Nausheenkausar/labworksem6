def sum_of_digits(n):
    """Function to calculate the sum of digits of a given decimal integer."""
    
    # Convert the number to positive if it's negative
    n = abs(n)  

    # Initialize sum variable
    digit_sum = 0  

    # Extract each digit and add to the sum
    while n > 0:
        digit_sum += n % 10  # Get the last digit and add to sum
        n //= 10  # Remove the last digit

    return digit_sum  

# Example usage
num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}.")
