# Read the input number
number = int(input())

# Check if the number is divisible by 3
if number % 3 == 0:
    # If divisible, print triple
    print(number * 3)
else:
    # If not divisible, print double
    print(number * 2)
