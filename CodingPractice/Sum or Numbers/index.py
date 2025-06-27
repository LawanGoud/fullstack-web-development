a = int(input())
b = int(input())

if a < 20 or b < 20 or (30 <= a + b < 50):
    print(a + b)
else:
    print(a)
    print(b)