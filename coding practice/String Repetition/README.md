### 🔁 String Repetition

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints the word **three times** in a single line, **separated by spaces**

---

### ✅ Python Code:

```python
word = input()
print(word + " " + word + " " + word)
```

---

### 🧠 Explanation:

- `input()` reads the word from the user.
- We use string concatenation with `" "` (a space) to repeat the word three times with spaces in between.

---

### 🧪 Example:

**Input:**

```
Hello
```

**Output:**

```
Hello Hello Hello
```

---

> 💡 You can also use string multiplication and `.join()` for cleaner code:

```python
word = input()
print(" ".join([word] * 3))
```
