n = int(input())

last_digit = str(n)[-1]

square = n ** 2 

square_last_digit = str(square)[-1]

if last_digit == square_last_digit:
    print("Equal")
else:
    print("Not Equal")