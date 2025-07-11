student_marks = int(input())

if student_marks >= 90:
    print("Discount is 200")
else:
    if student_marks >= 50:
        print("Discount is 100")
    else:
        print("No Discount")