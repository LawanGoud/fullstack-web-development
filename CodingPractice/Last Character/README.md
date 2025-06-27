### 🔚 Last Character

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **last character** of the word

---

### ✅ Python Code:

```python
word = input()
length = len(word)
print(word[length - 1])
```

---

### 🧠 Explanation:

- `input()` reads the word from the user.
- `len(word)` gives the total number of characters.
- `length - 1` gives the **index of the last character**.
- `word[length - 1]` accesses that character.
- `print()` displays it.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
n
```

---

> 💡 This method uses only indexing and length — perfect for beginners!
