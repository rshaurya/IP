# find if given year is a leap year or not
# a year is a leap year if 
# it is a multiple of 400 and 4 but not 100

y = int(input("Enter the year: "))
if y % 400 == 0 and y % 4 == 0:
    if y % 100 == 0:
        print(y, "is not  a leap year!")
else:
    print(y, "is a leap year.")