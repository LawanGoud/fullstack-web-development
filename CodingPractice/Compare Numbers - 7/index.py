n = input()

first_two = n[:2]
last_two = int(n[2:])

result = (first_two == "19") and (30 <= last_two <= 60)
print(result)
