# 4 WAP to check whether entered character is vowel or consonant.

ch = input("Enter Charecter = ")

vowel=('a','e','i','o','u','A','E','I','O','U')

if ch in vowel:
    print("The Entred Charecter is Vowel")

else:
    print("The Entred Charecter is Consol")


#________________Second method where we get only single charecter____________________

# # Get a single character input from the user
# char = input("Please enter a single character: ")

# # Check if the input is a single character
# if len(char) == 1 and char.isalpha():
#     # Convert the character to lowercase to handle both uppercase and lowercase vowels
#     char = char.lower()
    
#     # Check if the character is a vowel
#     if char in 'aeiou':
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is a consonant.")
# else:
#     print("Invalid input. Please enter exactly one alphabetic character.")
