## 🧩 **Problem Name:**

**Rectangle - 2**

---

## ❓ **Goal:**

Write a program that:

✅ Reads two numbers `M` (rows) and `N` (columns)
✅ Prints a rectangle of `M` rows and `N` columns
✅ Each column contains a `+` followed by a space
✅ Each row is printed on a new line

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `print()`
- String repetition

---

## ✅ **Code with Explanation:**

```python
# Read number of rows (M)
m = int(input())

# Read number of columns (N)
n = int(input())

# Create one line of N plus symbols with space
line = "+ " * n

# Counter for rows
row = 1

# Print the line M times
while row <= m:
    print(line)
    row = row + 1
```

---

## 🧪 **Sample Input:**

```
3
5
```

## 🧾 **Sample Output:**

```
+ + + + +
+ + + + +
+ + + + +
```

---
