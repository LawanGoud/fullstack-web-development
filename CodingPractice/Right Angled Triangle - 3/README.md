## 🧩 **Problem Name:**

**Right Angled Triangle - 3**

---

## ❓ **Goal:**

Write a program that:

✅ Reads a number `N`
✅ Prints a Right-Angled Triangle of `N` rows
✅ The first `N - 1` rows contain `*`
✅ The last (Nth) row contains `+`
✅ Each row repeats the symbol equal to the row number
✅ Each symbol is followed by a space

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `print()`
- String repetition
- Counters

---

## ✅ **Code with Explanation:**

```python
# Read the number of rows
n = int(input())

# Start from row 1
row = 1

# Repeat for rows 1 to N-1
while row < n:
    print(("* ")*row)  # Print * row times with space
    row = row + 1      # Move to next row

# Print the last row using +
print(("+ ")*n)
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
+ + + +
```

---
