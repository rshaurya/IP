
total = 0
name = input("Enter students' name: ")
ro = int(input("Enter roll number: "))
for i in range(1, 6):
    n = int(input('Enter marks for subject: '))
    total += n
print('Name:', name)
print('Total marks: ', total)
print("Percentage: ", (total / 500) * 100)
if total >= 90:
    print('Grade: A')
elif total >= 70 and total < 90:
    print('Grade: C')
elif total >= 50 and total < 70:
    print("Grade: C")
elif total > 40 and total < 50:
    print('Grade: D')
else:
    print('Grade: E')

