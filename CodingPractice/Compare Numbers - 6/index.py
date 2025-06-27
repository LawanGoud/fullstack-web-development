n = input()

first = int(n[0])
middle = int(n[1])
last = int(n[2])

result = (first > 4 and middle > 4 and last > 4) or (first == 6)
print(result)