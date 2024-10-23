#Write a Python program that asks the user to enter a number (1 to 7) and prints the
#corresponding day of the week. If the number is outside the 1-7 range, print "Invalid input"

# Ask the user for a number between 1 and 7
day_no = int(input("Enter a number (1-7): "))

if day_no == 1:
    day = "Monday"
elif day_no == 2:
    day = "Tuesday"
elif day_no == 3:
    day = "Wednesday"
elif day_no == 4:
    day = "Thursday"
elif day_no == 5:
    day = "Friday"
elif day_no == 6:
    day = "Saturday"
elif day_no == 7:
    day = "Sunday"
else:
    day = "Invalid input"
print(day)
