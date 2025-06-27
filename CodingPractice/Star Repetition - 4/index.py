word = input()

first_two = word[:2]
last_two = word[-2:]
middle_length = len(word) - 4 
middle_stars = "*" * middle_length

print(first_two + middle_stars + last_two)
