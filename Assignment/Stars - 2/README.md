### ✨ Stars - 2

**Task:**  
Write a program that reads a word and prints it surrounded by stars (`*`),  
where the number of stars before and after the word is equal to the **length** of the word.

---

### ✅ Example:

**Input:**

```
Python
```

**Output:**

```
****** Python ******
```

---

### ✅ Python Code:

```python
word = input()
stars = "*" * len(word)
print(stars + " " + word + " " + stars)
```

---

### 🧠 Explanation:

- `input()` reads the word from the user.
- `len(word)` calculates the length of the word.
- `"*"` is multiplied by the length to create the required number of stars.
- The final print joins:  
  **stars + space + word + space + stars**
