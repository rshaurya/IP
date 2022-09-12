# a box can hold 24 cookies
# container can hold 75 boxes
# input total number of cookies and find number of boxes and containers required

cookies = int(input("Enter total number of cookies: "))
print("You will need", cookies // 24, "boxes")
print("And ", cookies // 1800, "containers.")

