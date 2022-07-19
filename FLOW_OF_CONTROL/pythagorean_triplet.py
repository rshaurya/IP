# take the perpendicular, hypotenuse and base from a user and check whether they are a pythagorean triplet

p = int(input("Enter a perpendicular of a trianlge: "))
b = int(input("Enter a base of a triangle: "))
h = int(input("Enter a hypotenuse of a triangle: "))

if ( p ** 2 + b ** 2) == h ** 2:
    print(p,b,h, "form a pythagorean triplet")
else:
    print(p,b,h, "do not form a pythagorean triplet")