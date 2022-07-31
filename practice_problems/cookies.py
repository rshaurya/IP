# a box can hold 24 cookies
# container can hold 75 boxes
# input total number of cookies and find number of boxes and containers required

cookies = int(input("Enter total number of cookies: "))
print("You will need", cookies // 24, "boxes")
if cookies / 1800 < 1:
    print("You won't require one whole container. You lack ", 75 - (cookies//24), "boxes")

else:
    print("And ", cookies / 1800, "containers.")

