a = input()
b = input()
i = int(input())

part_from_a = a[i: i + len(b)]
result = part_from_a == b 
print(result)