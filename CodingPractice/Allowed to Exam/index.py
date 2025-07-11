hall_ticket = input()
identification = input()

if hall_ticket == "Y":
    print("Allowed to Exam - Has Hall ticket")
else:
    if identification == "Y":
        print("Allowed to Exam - Has Identification Card")