n = int(input())

total = 0
count = 0

while count < n:
    number = int(input())
    total += number
    count += 1

average = total / n
print(average)