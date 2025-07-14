A = int(input())  # Read the amount

notes_500 = A // 500
remaining = A % 500

notes_50 = remaining // 50
remaining = remaining % 50

notes_10 = remaining // 10
remaining = remaining % 10

notes_1 = remaining

print("500:", notes_500, "50:", notes_50, "10:", notes_10, "1:", notes_1)
