n = int(input())

group = n % 6

if group == 0:
    group = 6 

print("Group", group)