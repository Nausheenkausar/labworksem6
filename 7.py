def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]  # Slices the string in reverse order

# Taking input from the user
user_input = input("Enter a string: ")

# Reversing the string and displaying the result
reversed_str = reverse_string(user_input)
print("Reversed string:", reversed_str)
