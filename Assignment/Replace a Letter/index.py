word = input()
index = int(input())
character = input()

new_word = word[:index] + character + word[index + 1:]
print(new_word)
