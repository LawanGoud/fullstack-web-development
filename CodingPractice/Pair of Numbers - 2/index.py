a = int(input())
b = int(input())

div_by_3 = a % 3 == 0 and b % 3 == 0

div_by_12 = a % 12 == 0 or b % 12 == 0

if div_by_3 and div_by_12:
    print("Pair")
else:
    print("Not a Pair")