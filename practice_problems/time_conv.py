# take input from user in secs
# convert it in hrs, mins and secs

s = int(input("Enter number of seconds: "))
print(s, "seconds =  ", s / 3600, "hours")
print(s, "seconds = ", s % 3600, "mins")
print(s, "seconds = ", s % 60, "seconds")