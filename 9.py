
def count_case(string):
  """Counts the number of uppercase and lowercase letters in a string."""

  upper_count = 0
  lower_count = 0

  for char in string:
    if char.isupper():
      upper_count += 1
    elif char.islower():
      lower_count += 1

  return upper_count, lower_count

# Example usage:
string =input(f"enter a sentence:")
upper, lower = count_case(string)
print("Uppercase:", upper)
print("Lowercase:", lower)
