text = input()
n = int(input())

first_part = text[:n]
last_part = text[-n:]

result = first_part != last_part
print(result)