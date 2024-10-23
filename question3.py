#Write a program that takes a score (0-100) as input and categorizes it into one of the following
#grades:
#● A (90-100)
#● B (80-89)
#● C (70-79)
#● D (60-69)
#● F (below 60)
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade for the score {score} is: {grade}")
