## 🧩 **Problem Name:**

**Print the Characters**

---

## 🎯 **Goal:**

✅ Read a word (string)
✅ Print **each character** of the word on a **new line**

---

## 🧠 **Concepts Used:**

- Input/output
- String indexing
- `while` loop
- `len()` function

---

## ✅ **Code with Explanation:**

```python
# Read the input string
word = input()

# Get the length of the string
length = len(word)

# Set a counter to 0
index = 0

# Loop through the string using a while loop
while index < length:
    print(word[index])  # Print the character at current index
    index = index + 1   # Move to the next character
```

---

## 🧪 **Sample Input:**

```
shine
```

## 🧾 **Sample Output:**

```
s
h
i
n
e
```

---
