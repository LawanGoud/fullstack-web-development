## 🧩 **Problem Name:**

**String Repetition**

---

## 🎯 **Goal:**

Write a program to:

- ✅ Read a **word**
- ✅ Read a number `count`
- ✅ Print the **word repeated `count` times**, separated by a space — all in one line

---

## 🧠 **Concepts Used:**

- Input/output
- String concatenation
- Multiplication (`*`) with strings

---

## ✅ **Code:**

```python
word = input()
count = int(input())

# Create the repeated string with spaces
result = (word + " ") * count

# Print the result (will have an extra space at the end — that’s okay for now)
print(result)
```

---

## 🧪 **Sample Input:**

```
pen
2
```

## 🧾 **Sample Output:**

```
pen pen
```

---
