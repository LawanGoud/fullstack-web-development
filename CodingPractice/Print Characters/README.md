## 🧩 **Problem Name:**

**Print Characters**

---

## 🎯 **Goal:**

✅ Read a word
✅ Print each character of the word on a **new line**

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- String length (`len()`)
- Character access using index

---

## ✅ **Code with Explanation:**

```python
# Read the word from input
word = input()

# Start from the first index (position 0)
index = 0

# Repeat until we reach the end of the word
while index < len(word):
    print(word[index])  # Print character at current index
    index = index + 1   # Move to the next character
```

---

## 🧪 **Sample Input:**

```
Python
```

## 🧾 **Sample Output:**

```
P
y
t
h
o
n
```

---
