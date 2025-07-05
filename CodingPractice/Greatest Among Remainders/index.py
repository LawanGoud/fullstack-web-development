n = int(input())

r1 = n % 4
r2 = n % 5

if r1 > r2:
    print(r1)
elif r2 > r1:
    print(r2)