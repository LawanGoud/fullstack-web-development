## 🧩 **Problem Name:**

**Equal to**

---

## 📝 **Task:**

Write a program that:

- Reads **two words** from the user
- Checks if the **two words are the same** (equal)
- Prints `True` if they are equal, otherwise `False`

---

## 💡 **Concepts Used:**

- `input()` to take input
- `==` (equality operator) to compare strings
- `print()` to display result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Take the first word as input

```python
word1 = input()
```

This will read the first word, e.g., `"Jam"`.

---

### ✅ Step 2: Take the second word as input

```python
word2 = input()
```

This will read the second word, e.g., `"Jam"`.

---

### ✅ Step 3: Compare the two words

```python
result = word1 == word2
```

- The `==` operator checks if both words are **exactly the same** (same letters and case).
- If `word1` and `word2` are equal, it returns `True`; otherwise, `False`.

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read first word
word1 = input()

# Step 2: Read second word
word2 = input()

# Step 3: Check if they are equal
result = word1 == word2

# Step 4: Print result
print(result)
```

---

## 🧪 Sample Input:

```
Jam
Jam
```

## 🎯 Sample Output:

```
True
```

---
