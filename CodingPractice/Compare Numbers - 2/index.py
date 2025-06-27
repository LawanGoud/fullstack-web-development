a = int(input())
b = int(input())

one_negative = a < 0 or b < 0 

sum_greater_than_7 = (a + b) > 7 

result = one_negative and sum_greater_than_7

print(result)