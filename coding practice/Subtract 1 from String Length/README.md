### ➖ Subtract 1 from String Length

**Task:**  
Write a Python program that:

- Reads a word as input
- Calculates the **length** of the word
- Prints the result of `length - 1`

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
- `len(word)` gives the total number of characters.
- We subtract `1` from the length and print the result.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
5
```

---

> ℹ️ Useful when you need to work with positions or characters **excluding** the last one.
