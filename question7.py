#Write a Python program that takes the lengths of three sides of a triangle as input and
#determines if the triangle is:
#● Equilateral (all sides are equal),
#● Isosceles (two sides are equal), or
#● Scalene (all sides are different).


side1 = float(input("Enter your first side length: "))
side2 = float(input("Enter your first side length: "))
side3 = float(input("Enter your first side length: "))

if side1 == side2 == side3:
    triangle = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle = "Isosceles"
else:
    triangle = "Scalene"
print(f"this is {triangle} triangle")
