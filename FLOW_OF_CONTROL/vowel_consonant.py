# take a letter from the user and tell if it is a vowel or consonant

s = input("Enter any small letter: ")
if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print(s, "is a vowel")
else:
    print(s, "is a consonant")

# Alternative method including capital and small letters
a = input("Enter a letter: ")
l = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
if a in l:
    print(a, "is a vowel")
else:
    print(a, "is a consonant")
