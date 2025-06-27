word1 = input()
word2 = input()

last3_word1 = word1[-3:]
last3_word2 = word2[-3:]

result = last3_word1 == last3_word2 
print(result)
