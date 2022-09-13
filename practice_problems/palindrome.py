
s = input('Enter a string: ')
st = ""

for i in range(len(s)):
    st += s[-i]
print(st)
