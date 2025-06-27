m = int(input())
p = int(input())
c = int(input())

result = (m >= 70 and p >= 60 and c >= 60) or (m + p + c >= 180)

print(result)