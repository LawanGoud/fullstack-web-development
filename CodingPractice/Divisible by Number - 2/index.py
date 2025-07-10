# Read the number

number = int(input())

# Calculate the triple of the number

triple_of_number = 3 * number

# check if the triple is divisible by 6

if triple_of_number % 6 == 0:
    print(triple_of_number)
else:
    print(number)