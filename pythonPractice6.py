"""
R. Malstrom

Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)

Last modified: 9.24.2024
"""

userString = str(input("Please enter a word: "))
emptyString = ""

for c in userString:
    emptyString = c + emptyString

if emptyString == userString:
    print(f'{userString} is a palindrome')
else:
    print(f'{userString} is not a palindrome')