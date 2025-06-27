### ⭐ Star Repetition - 3

**Task:**  
Write a program that reads a string and:

- Prints the **first** and **last** characters of the string,
- Replacing the characters in between with `*`.

---

### ✅ Example

**Input:**

```
python
```

**Output:**

```
p****n
```

---

### ✅ Python Code

```python
word = input()

# Get first character
first = word[0]

# Get last character
last = word[len(word) - 1]

# Number of stars in the middle
stars = "*" * (len(word) - 2)

# Combine and print
print(first + stars + last)
```

---

### 🧠 Explanation

- `word[0]` gives the first character.
- `word[len(word) - 1]` gives the last character.
- `(len(word) - 2)` gives the number of middle characters, which we replace with `"*"`.
- The final result is formed by joining `first + stars + last`.
