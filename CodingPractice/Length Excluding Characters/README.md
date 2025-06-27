### ➖ Length Excluding First and Last Characters

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **length excluding** the first and last characters

---

### ✅ Python Code:

```python
word = input()
length = len(word)
print(length - 2)
```

---

### 🧠 Explanation:

- `input()` reads the word.
- `len(word)` gives the total number of characters.
- Since we want to exclude the **first** and **last** characters, we subtract 2 from the length.
- `print()` displays the result.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
4
```

---

> ℹ️ This is useful when processing only the **middle part** of a word.
