student_marks = float(input())

if student_marks > 85:
    print("A")
elif student_marks > 70 and student_marks <= 85:
    print("B")
elif student_marks >= 60 and student_marks <= 70:
    print("C")
else:
    print("F")