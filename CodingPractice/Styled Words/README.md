🧩 **Problem Name:**  
Styled Word (Hyphen Separated Characters, Basic For Loop)

❓ **Goal:**  
✅ Read a word  
✅ Print the characters of the word separated by hyphens (`-`), all on a single line  
✅ Use only basic concepts you’ve learned so far: `input()`, `len()`, `for` loop, string concatenation, and `print()`  
✅ Do not use `if` statements or advanced `print()` parameters like `sep` or `end`

🧠 **Concepts Used:**

- `input()`
- `len()`
- `for` loop
- String concatenation
- `print()`

✅ **Code with Explanation:**

```python
# Read a word from the user
word = input()

# Find the length of the word
word_length = len(word)

# Start the output string with the first character of the word
hyphenated_output = word[0]

# Loop from the second character to the last character
for index in range(1, word_length):
    # Add a hyphen and the current character to the output string
    hyphenated_output = hyphenated_output + "-" + word[index]

# Print the final hyphen-separated string
print(hyphenated_output)
```

### Explanation:

- We use `input()` to get the word from the user and store it in `word`.
- The length of the word is found using `len(word)`, stored in `word_length`.
- We initialize the `hyphenated_output` string with the first character so that the output does not begin with a hyphen.
- Then, using a `for` loop from the second character (index 1) to the end of the word, we add a hyphen followed by the current character to `hyphenated_output`.
- Finally, `print()` outputs the fully constructed string containing the characters separated by hyphens.

🧪 **Sample Input:**

```
Python
```

🧾 **Sample Output:**

```
P-y-t-h-o-n
```
