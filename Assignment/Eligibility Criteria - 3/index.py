m = int(input())
p = int(input())
c = int(input())

condition1 = m >= 35 and p >= 35 and c >= 35 

condition2 = m + p >= 90 or p + c >= 90 or m + c >= 90

result = condition1 and condition2

print(result)