def is_narcissistic(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n

def find_narcissistic_numbers(n):
    start = 10**(n-1)  # Smallest n-digit number
    end = 10**n        # Largest n-digit number
    narcissistic_numbers = [i for i in range(start, end) if is_narcissistic(i)]
    return narcissistic_numbers

# Example usage
n = int(input("Enter the number of digits: "))
result = find_narcissistic_numbers(n)
print(f"Narcissistic numbers with {n} digits: {result}")
