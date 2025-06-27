m = int(input())
p = int(input())
c = int(input())

condition1 = (m + p >= 100) or (p + c >= 100) or (m + c >= 100)
condition2 = m + p + c >= 180 

result = condition1 and condition2 
print(result)