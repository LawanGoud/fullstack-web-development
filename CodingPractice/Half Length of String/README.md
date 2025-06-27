### 🔢 Half Length of String

**Task:**  
Write a Python program that:

- Reads a word as input
- Calculates and prints **half the length** of the word

---

### ✅ Python Code:

```python
word = input()
length = len(word)
print(length // 2)
```

---

### 🧠 Explanation:

- `input()` reads the word.
- `len(word)` gives the total number of characters.
- `//` is used for **integer division** (to avoid decimal values).
- `length // 2` gives the **whole number** result of dividing the length by 2.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
3
```

---

> 💡 Use `//` to ensure the result is an integer (no decimals).
