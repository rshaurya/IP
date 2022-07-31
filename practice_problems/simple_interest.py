# calculate simple interest and total amount to be paid by person

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

si = p * r * t / 100

print("Simple interest: ", si)
print("Total amount to be paid: ", si + p)
