# find the greater number

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# method 1
if n1 > n2:
    print(n1, "is greater than", n2)
else:
    print(n2, "is greater than", n1)

# method 2
l = []
l.append(n1)
l.append(n2)
print(max(l), "is greater.")
