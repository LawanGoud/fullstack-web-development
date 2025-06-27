maths = int(input())
physics = int(input())

if (maths > 35 and physics > 35) or (maths + physics >= 100):
    print("Qualified")
else:
    print("Not Qualified")