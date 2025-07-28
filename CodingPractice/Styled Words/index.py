word = input("Enter a word: ")

word_length = len(word)

hyphenated_word = word[0]

for index in range(1,word_length):
    hyphenated_word += "-" + word[index]

print(hyphenated_word)