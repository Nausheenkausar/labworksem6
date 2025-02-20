def count_and_display_vowels(text):
    
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    vowel_count = 0
    found_vowels = []

    # Iterate through the text and check for vowels
    for char in text:
        if char in vowels:
            vowel_count += 1
            found_vowels.append(char)

    return vowel_count, found_vowels

# Taking input from the user
user_input = input("Enter a text: ")

# Calling the function to count and display vowels
count, vowels = count_and_display_vowels(user_input)

# Displaying the results
print(f"Number of vowels: {count}")
print(f"Vowels in the text: {vowels}")
