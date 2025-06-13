### 🔡 First & Last Characters

**Task:**  
Write a program that reads a word and prints:

- the **first character** on the first line
- the **last character** on the second line

---

### ✅ Example

**Input:**

```
qwerty
```

**Output:**

```
q
y
```

---

### ✅ Python Code

```python
word = input()
print(word[0])
print(word[len(word) - 1])
```

---

### 🧠 Explanation

- `word[0]` gives the **first character** of the string.
- `word[len(word) - 1]` gives the **last character**.
- Indexing in Python starts at 0, so the last index is `length - 1`.

```

```
