### ⭐ Star Repetition

**Task:**  
Write a Python program that:

- Reads a word as input
- Prints a line of stars (`*`) equal to the **length of the word**

---

### ✅ Python Code:

```python
word = input()
length = len(word)
print("*" * length)
```

---

### 🧠 Explanation:

- `input()` reads a word from the user.
- `len(word)` calculates how many characters are in the word.
- `"*"` is multiplied by that number to repeat the star.
- `print()` displays the repeated stars.

---

### 🧪 Example:

**Input:**

```
hello
```

**Output:**

```
*****
```

---

> 💡 This creates a simple visual representation where each character in the word is matched by a star.
