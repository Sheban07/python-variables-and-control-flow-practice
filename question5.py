#Write a Python program that asks the user for their age and tells them whether they are a minor
#(under 18), an adult (18-65), or a senior (over 65).

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 65:
    print("You are a senior")
else:
    print("You are an adult")

