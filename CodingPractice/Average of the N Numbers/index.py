limit = int(input())

number = 1 
total = 0

while number <= limit:
    total += number
    number += 1

average = total / limit
print(average)