a = int(input())
b = int(input())

one_less_than_60 = a < 60 or b < 60

one_greater_than_80 = a > 80 or b > 80 

result = one_less_than_60 and one_greater_than_80

print(result)