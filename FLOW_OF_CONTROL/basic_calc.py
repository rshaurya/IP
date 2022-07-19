# take 2 numbers from the user
# take an operator and perform the operation with the 2 numbers

n1 = int(input("Enter any single digit number: "))
n2 = int(input("Enter any single digit number: "))
print("The operators available are: +, -, *, /")
op = input("Enter any operator: ")

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print("Please recheck the given operator")