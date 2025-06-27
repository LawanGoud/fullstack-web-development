a = input()
b = input()

length_of_b = len(b)

last_part_of_a = a[-length_of_b:]
print(last_part_of_a == b)
