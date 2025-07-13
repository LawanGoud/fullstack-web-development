attendance_input = input()

has_medical_report = input()

attendance_value = int(attendance_input[:-1])

if attendance_value >= 75 or has_medical_report == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")