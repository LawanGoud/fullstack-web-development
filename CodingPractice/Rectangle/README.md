## 🧩 **Problem Name:**

**Rectangle **

---

## ❓ **Goal (Question Rewritten):**

Write a program that:

✅ Reads two numbers:
    `M` → number of rows
    `N` → number of columns

✅ Prints a rectangle of stars `*` with `M` rows and `N` columns
✅ Each row should have `N` stars separated by a space
✅ Use only basic concepts (no `strip`, no nested loops)

---

## 🧠 **Concepts Used:**

- Input and output
- Integer conversion using `int()`
- Loop using `while`
- String repetition using `*`
- Simple variable assignment and increment

---

## ✅ **Code with Explanation:**

```python
# Read the number of rows (M)
rows = int(input())

# Read the number of columns (N)
cols = int(input())

# Create one line of stars using string repetition
line = "* " * cols  # This creates a single line of stars (with spaces)

# Start a counter for rows
count = 1

# Print the line 'rows' number of times
while count <= rows:
    print(line)  # Prints one row of the rectangle
    count = count + 1  # Move to the next row
```

---

## 🧪 **Sample Input:**

```
4
5
```

## 🧾 **Sample Output:**

```
* * * * *
* * * * *
* * * * *
* * * * *
```

---
