### 🔤 First Character

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **first character** of the word

---

### ✅ Python Code:

```python
word = input()
print(word[0])
```

---

### 🧠 Explanation:

- `input()` reads the word from the user.
- `word[0]` accesses the first character of the string (indexing starts at 0).
- `print()` displays that character.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
P
```

---

> ⚠️ If the input is empty, trying to access `word[0]` will cause an `IndexError`. You can add a check to handle that if needed.
