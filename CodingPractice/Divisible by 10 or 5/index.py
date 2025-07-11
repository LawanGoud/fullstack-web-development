number = int(input())

if number % 10 == 0:
    print("Divisible by 10")
else:
    if number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not Divisible by 10 or 5")