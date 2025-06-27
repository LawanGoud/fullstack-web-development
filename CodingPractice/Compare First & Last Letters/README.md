## 🧩 **Problem Name:**

**Compare First & Last Letters**

---

## 📝 **Task:**

Write a program that:

- Reads a word.
- Checks if the **first letter** and **last letter** of the word are **not the same**.
- Prints `True` if they are different, otherwise prints `False`.

---

## 💡 **Concepts Used:**

- `input()` – to get the word
- String indexing (`word[0]`, `word[-1]`)
- Relational operator `!=` – checks if two values are not equal
- `print()` – to show the result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the word from the user

```python
word = input()
```

### ✅ Step 2: Get the first and last letters

- First letter: `word[0]`
- Last letter: `word[-1]` (or `word[len(word) - 1]`)

### ✅ Step 3: Compare them using `!=`

```python
result = word[0] != word[-1]
```

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read input
word = input()

# Step 2: Compare first and last letters
result = word[0] != word[-1]

# Step 3: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
Python
```

## 🎯 Sample Output:

```
True
```
