# take a two digit number from the user and check whether it is a speacial number or not
# input = ab
# ab will be a special number when (a+b) + (a*b) = ab

# METHOD 1:
# num = int(input("Enter any two digit number: "))
# d1 = num % 10
# d2 = num // 10
# if (d1 + d2) + (d1 * d2) == num:
#     print(num, "is a special number")
# else:
#     print(num, "is not a special number")

# METHOD 2
num = input("Enter any two digit number: ")
if ( int(num[0]) + int(num[1]) ) + ( int(num[0]) * int(num[1]) ) == int(num):
    print(num, "is a special number")
else:
    print(num, "is not a special number")