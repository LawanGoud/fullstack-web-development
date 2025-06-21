a = int(input())
b = int(input())

both_positive = a > 0 and b > 0

both_less_than_70 = a < 70 and b < 70

result = both_positive or both_less_than_70

print(result)
