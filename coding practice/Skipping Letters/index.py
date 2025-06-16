word = input()
index = int(input())

part1 = word[:index]
part2 = word[index + 1:]

new_word = part1 + part2
print(new_word)