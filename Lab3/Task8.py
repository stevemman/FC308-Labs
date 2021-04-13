# Ask the user to enter a grade.
percentage_grade = int(input("Please give me a percentage grade : "))

# Check which range the grade belongs and print the appropriate letter grade.
if percentage_grade <= 100 and percentage_grade >= 80:
    print("A")
elif percentage_grade <= 79 and percentage_grade >= 60:
    print("B")
elif percentage_grade <= 59 and percentage_grade >= 40:
    print("C")
elif percentage_grade <= 39 and percentage_grade >= 20:
    print("D")
elif percentage_grade <= 19 and percentage_grade >= 0:
    print("F")
else:
    print("The grade is outside the 0-100 range")
