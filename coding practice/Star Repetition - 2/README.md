### ⭐ Star Repetition - 2

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **first letter** as it is
- Replaces all **other letters** with stars (`*`)

---

### ✅ Python Code:

```python
word = input()
length = len(word)
stars = "*" * (length - 1)
print(word[0] + stars)
```

---

### 🧠 Explanation:

- `input()` reads the word.
- `len(word)` gives the total number of characters.
- We keep the **first character** using `word[0]`.
- Then we create a string of `*` equal to the **remaining characters**.
- We join them using `+` and print the result.

---

### 🧪 Example:

**Input:**

```
hello
```

**Output:**

```
h****
```

---

> 💡 This is a simple way to hide part of a word or simulate password masking.
