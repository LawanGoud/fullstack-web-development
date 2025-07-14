D = int(input())  # Read the day number

if D == 1 or D == 2:
    print("Week Start")
elif D == 3 or D == 4 or D == 5:
    print("Midweek")
else:
    print("Weekend")
