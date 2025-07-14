A = int(input())  # Read the amount

notes_100 = A // 100         # Count of ₹100 notes
remaining = A % 100

notes_50 = remaining // 50   # Count of ₹50 notes
remaining = remaining % 50

notes_10 = remaining // 10   # Count of ₹10 notes
remaining = remaining % 10

notes_1 = remaining          # Count of ₹1 coins

print("100 :", notes_100)
print("50 :", notes_50)
print("10 :", notes_10)
print("1:", notes_1)
