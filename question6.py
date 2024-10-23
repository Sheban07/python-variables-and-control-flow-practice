#Write a Python program that asks the user to enter a password. If the password is "python123",
#print "Access granted." Otherwise, print "Access denied."

password = "python123"

access = input("Enter your password: ")
if password == access:
    print("Access granted")
else:
    print("Access denied")
