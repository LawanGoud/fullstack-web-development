## 🧩 **Problem Name:**

**Right Angled Triangle**

---

## ❓ **Goal (Question Rewritten):**

Write a program that:

✅ Reads a number `N`
✅ Prints a right-angled triangle of `N` rows
✅ Each row should have increasing number of `*` (stars), starting from 1
✅ Use only basic concepts you've already learned (no nested loops)

---

## 🧠 **Concepts Used:**

- Input using `input()`
- Integer conversion using `int()`
- `while` loop
- String repetition using `*`
- Counter variables

---

## ✅ **Code with Explanation:**

```python
# Read the number of rows for the triangle
rows = int(input())

# Start with the first row
count = 1

# Loop from 1 to N
while count <= rows:
    print("* " * count)  # Print 'count' number of stars followed by space
    count = count + 1     # Move to the next row
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
