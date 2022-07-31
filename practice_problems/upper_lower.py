# find if the alphabet is uppercase or lowercase

char = input("Enter any alphabet (uppercase or lowercase): ")
if char == char.lower():
    print(char, "is a lowercase character")
elif char == char.upper():
    print(char, "is an uppercase character")
