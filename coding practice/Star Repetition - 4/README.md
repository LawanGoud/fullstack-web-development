## 🧩 Problem Name

**Star Repetition - 4**

---

## 📝 Task

Write a program that:

- Reads a **word** as input.
- Prints:

  - The **first two letters**,
  - Then **stars (`*`)** in place of all **middle letters**,
  - Then the **last two letters**.

---

## 🧠 Concept Explanation

We will use only **learned concepts**:

✅ `input()` to read a string
✅ `print()` for output
✅ String indexing like `word[0]`, `word[1]`, etc.
✅ String slicing
✅ String repetition using `*`

### 💡 Logic

1. Get the first two characters → `word[:2]`
2. Get the last two characters → `word[-2:]`
3. Calculate how many middle characters need to be replaced with `*` → `len(word) - 4`
4. Generate that many stars → `"*" * middle_length`
5. Combine them: first part + stars + last part

---

## ✅ Final Code

```python
word = input()

first_two = word[:2]
last_two = word[-2:]
middle_length = len(word) - 4
middle_stars = "*" * middle_length

print(first_two + middle_stars + last_two)
```

---

## 🧪 Sample Input

```
message
```

## 🎯 Sample Output

```
me***ge
```

---
