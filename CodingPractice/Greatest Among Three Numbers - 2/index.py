first_value = int(input())
second_value = int(input())
third_value = int(input())

if first_value > second_value:
    if first_value > third_value:
        print(first_value)
    else:
        print(third_value)
else:
    if second_value > third_value:
        print(second_value)
    else:
        print(third_value)