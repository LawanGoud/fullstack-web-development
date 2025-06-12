### 🔚 Index of Last Character

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **index** of the last character in the word

---

### ✅ Python Code:

```python
word = input()
length = len(word)
print(length - 1)
```

---

### 🧠 Explanation:

- `input()` reads the word as a string.
- `len(word)` gives the number of characters in the word.
- Since indexing starts from `0`, the last character is at position `length - 1`.
- `print()` displays that index.

---

### 🧪 Example:

**Input:**

```
hello
```

**Output:**

```
4
```

---

> 💡 Indexing starts from `0`, so the last index is always one less than the total length.
