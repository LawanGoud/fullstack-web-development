### 🖨️ Print the Input - 3

**Task:**  
Write a Python program that:

- Reads **two words** as input (one after another)
- Prints each word on a **separate line**

---

### ✅ Python Code:

```python
word1 = input()
word2 = input()
print(word1)
print(word2)
```

---

### 🧠 Explanation:

1. `input()` is called twice to read two separate words.
2. `word1` stores the first input, and `word2` stores the second input.
3. Each word is printed on its own line using two `print()` statements.

---

### 🧪 Example:

**Input:**

```
Hello
Python
```

**Output:**

```
Hello
Python
```

---

> 💡 If both words are entered on the same line, use `input().split()` instead.

```python
word1, word2 = input().split()
print(word1)
print(word2)
```
