a = int(input())
b = int(input())
c = int(input())

result = (a + b > c) and (a + c > b) and (b + c > a)

print(result)