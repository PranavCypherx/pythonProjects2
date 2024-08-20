#write a program that calculate and displays the letter grade
#Grade as A, B, C, D, E, F
#Input is in int

score = int(input("Enter your score\n"))

#score >=90 and score <=100 -> "A"
#score >=80 and score <=89 -> "B"

if score >= 90 and score <=99 :
    grade = "A"
    print("Your grade is", grade)
elif score >= 80 and score <=89 :
    grade = "B"
    print("Your grade is", grade)
elif score >= 70 and score <=79 :
    grade = "C"
    print("Your grade is", grade)
elif score >= 60 and score <=69 :
    grade = "D"
    print("Your grade is", grade)
elif score >= 50 and score <=59 :
    grade = "E"
elif score >= 100 :
    grade = "O"
    print("Outstanding Performance")
else :
    print("You are Fail", grade)