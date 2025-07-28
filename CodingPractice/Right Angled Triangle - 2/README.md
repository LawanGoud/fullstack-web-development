## 🧩 **Problem Name:**

**Right Angled Triangle - 2**

---

## ❓ **Goal (Question Rewritten):**

Write a program that:
✅ Reads a number `N`
✅ Prints a right-angled triangle of `N` rows
✅ Each row contains the same number repeated (row number), with spaces after each number
✅ Example:

```
Input: 4
Output:
1
2 2
3 3 3
4 4 4 4
```

---

## 🧠 **Concepts Used:**

- Input using `input()`
- Integer conversion using `int()`
- `while` loop
- String multiplication using `*`
- Counter variables

---

## ✅ **Code with Explanation:**

```python
# Read the number of rows for the triangle
rows = int(input())

# Start with the first row
count = 1

# Repeat the loop for each row
while count <= rows:
    # Create the pattern: repeat the number with a space, 'count' times
    print((str(count) + " ") * count)
    count = count + 1  # Move to the next row
```

---

## 🧪 **Sample Input:**

```
4
```

## 🧾 **Sample Output:**

```
1
2 2
3 3 3
4 4 4 4
```

---
