## 🧩 **Problem Name:**

**Rectangle - 3**

---

## ❓ **Goal:**

Write a program that:
✅ Reads two numbers `M` (rows) and `N` (columns)
✅ Prints a rectangle of `M` rows and `N` columns
✅ Each row contains the same number repeated `N` times
✅ Each number is followed by a space
✅ Each row is printed on a new line

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `print()`
- String repetition
- Number to string conversion (`str()`)

---

## ✅ **Code with Explanation:**

```python
# Read number of rows (M)
m = int(input())

# Read number of columns (N)
n = int(input())

# Initialize row counter
row = 1

# Loop to print M rows
while row <= m:
    # Create the row using the current row number repeated N times with space
    line = (str(row) + " ") * n
    print(line)
    row = row + 1
```

---

## 🧪 **Sample Input:**

```
3
4
```

## 🧾 **Sample Output:**

```
1 1 1 1
2 2 2 2
3 3 3 3
```

---
