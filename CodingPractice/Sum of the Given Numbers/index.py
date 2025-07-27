total_numbers = int(input())

sum_of_numbers = 0

count = 1 

while count <= total_numbers:
    current_number = int(input())
    sum_of_numbers = sum_of_numbers + current_number
    count = count + 1

print(sum_of_numbers)