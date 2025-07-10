first_number = int(input())
second_number = int(input())

remainder1 = first_number % second_number
remainder2 = second_number % first_number

if remainder1 < remainder2:
    print(remainder1)
else:
    print(remainder2)