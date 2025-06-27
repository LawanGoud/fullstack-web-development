m = int(input())
p = int(input())
c = int(input())

condition1 = m >= 60 and p >= 50 and c >= 45 and (m + p + c >= 180)

condition2 = (m + p >= 120) or (c + p >= 110)

result = condition1 or condition2 

print(result)