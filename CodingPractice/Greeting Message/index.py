current_hour = int(input())

if current_hour >= 4 and current_hour < 12:
    print("Good Morning")
elif current_hour >= 12 and current_hour < 16:
    print("Good Afternoon")
elif current_hour >= 16 and current_hour < 20:
    print("Good Evening")
else:
    print("Good Night")