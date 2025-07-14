# Read first day name
first_day = input()

# Read the date number
date = int(input())

# Convert first day name to a number (1 to 7)
if first_day == "Monday":
    start = 1
elif first_day == "Tuesday":
    start = 2
elif first_day == "Wednesday":
    start = 3
elif first_day == "Thursday":
    start = 4
elif first_day == "Friday":
    start = 5
elif first_day == "Saturday":
    start = 6
else:
    start = 7  # Sunday

# Find the day number for the given date
# (date - 1) days after the first day
day_num = (start + (date - 1)) % 7

# Adjust 0 to 7 (since modulo 7 can return 0)
if day_num == 0:
    day_num = 7

# Convert day number back to day name
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
else:
    print("Sunday")
