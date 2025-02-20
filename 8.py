def reverse_words_in_string(s):
    
    words = s.split()  
    reversed_words = ' '.join(reversed(words))  
    return reversed_words

# Taking input from the user
user_input = input("Enter a string: ")

# Reversing the words and displaying the result
reversed_str = reverse_words_in_string(user_input)
print("String with reversed words:", reversed_str)
