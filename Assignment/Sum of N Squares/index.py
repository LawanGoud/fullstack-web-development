n = int(input())

num = 1

sum_of_squares = 0

while num <= n:
    sum_of_squares += num * num
    num += 1

print(sum_of_squares)