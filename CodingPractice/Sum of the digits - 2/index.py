number = int(input())

digit_sum = 0

if number >= 10000:
    digit_sum += number // 10000
    number = number % 10000

if number >= 1000:
    digit_sum += number // 1000
    number = number % 1000

if number >= 100:
    digit_sum += number // 100
    number = number % 100

if number >= 10:
    digit_sum += number // 10
    number = number % 10

digit_sum += number

print(digit_sum)