w1 = input()
w2 = input()

length = len(w2)

first_part = "*" * length
second_part = w1[length:]

print(first_part + second_part)
