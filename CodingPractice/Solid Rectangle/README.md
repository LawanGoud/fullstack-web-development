## 🧩 **Problem Name:**

**Solid Rectangle**

---

## 🎯 **Goal:**

✅ Read two integers `M` and `N`
✅ Print `M` rows
✅ Each row should have `N` asterisks separated by space
✅ Use only what you've learned (no nested loops or lists)

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- String repetition using `*`
- `print()` function with formatting

---

## ✅ **Code:**

```python
# Read number of rows
rows = int(input())

# Read number of columns
columns = int(input())

# Create one row of stars using repetition
row_of_stars = ("* " * columns).strip()

# Use a loop to print the row M times
count = 1
while count <= rows:
    print(row_of_stars)
    count = count + 1
```

---

## 🧪 **Sample Input:**

```
2
3
```

## 🧾 **Sample Output:**

```
* * *
* * *
```

---
