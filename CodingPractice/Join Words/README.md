### 🔗 Join Words

**Task:**  
Write a Python program that:

- Reads **two words** as input
- Prints a **single word** formed by **joining** the two words (no space between them)

---

### ✅ Python Code:

```python
word1 = input()
word2 = input()
result = word1 + word2
print(result)
```

---

### 🧠 Explanation:

1. `input()` reads two words from the user (one per line).
2. `word1 + word2` joins them using string concatenation.
3. `print(result)` outputs the joined word.

---

### 🧪 Example:

**Input:**

```
code
camp
```

**Output:**

```
codecamp
```

---

> 💡 If you want a space between the words, use `word1 + " " + word2` instead.
