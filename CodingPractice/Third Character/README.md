### 🔤 Third Character

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the **third character** of the word

---

### ✅ Python Code:

```python
word = input()
print(word[2])
```

---

### 🧠 Explanation:

- `input()` reads the word from the user.
- `word[2]` accesses the **third character** of the word (since indexing starts at 0).
- `print()` displays that character.

---

### 🧪 Example:

**Input:**

```
Python
```

**Output:**

```
t
```

---

> ⚠️ Make sure the word has at least 3 characters. Otherwise, `word[2]` will raise an `IndexError`.
