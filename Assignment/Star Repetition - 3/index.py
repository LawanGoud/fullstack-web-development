word = input()

first = word[0]

last = word[len(word) - 1]

stars = "*" * (len(word) - 2)

print(first + stars + last)