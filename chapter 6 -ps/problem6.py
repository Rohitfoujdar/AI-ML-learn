student_marks = int(input("Enter your marks : "))

if(student_marks <=100 and student_marks > 90):
     grade = "EX"
elif(student_marks<90 and student_marks >=80):
     grade = "A"
elif(student_marks<80 and student_marks >= 70):
     grade = "B"
elif(student_marks<70 and student_marks >= 60):
     grade = "C"
elif(student_marks<60 and student_marks >= 50):
     grade = "D"
elif(student_marks<50):
     grade = "F"

print(grade)