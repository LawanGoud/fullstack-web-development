year = int(input())

is_divisible_by_400 = (year % 400 == 0)

is_divisible_by_4_not_100 = (year % 4 == 0) and (year % 100 != 0)

if is_divisible_by_400 or is_divisible_by_4_not_100:
    print(True)
else:
    print(False)