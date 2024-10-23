#Write a Python program that asks the user for a number and then prints whether the number is
#odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

