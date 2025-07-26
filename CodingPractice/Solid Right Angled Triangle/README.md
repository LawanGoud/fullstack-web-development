## 🧩 **Problem Name:**

**Solid Right-Angled Triangle**

---

## 🎯 **Goal:**

✅ Read an integer `N`
✅ Print a triangle of `N` rows using `*`
✅ Each row `i` should have `i` asterisks

---

## 🧠 **Concepts Used:**

- Input
- `while` loop
- Counters
- String multiplication
- Simple print formatting

---

## ✅ **Code:**

```python
# Read number of rows
rows = int(input())

# Initialize row number
i = 1

# Loop through each row
while i <= rows:
    # Print i stars with space
    print("* " * i)
    i = i + 1
```

---

## 🧪 **Sample Input:**

```
4
```

## 🧾 **Sample Output:**

```
*
* *
* * *
* * * *
```

---
