## 🧩 **Problem Name:**

**Two Right Angled Triangles**

---

## ❓ **Goal:**

Write a program that:

✅ Reads a number `N`
✅ Prints **two right-angled triangles** of `N` rows
✅ Each row prints the row number, repeated that many times
✅ Each number is followed by a space
✅ Both triangles are printed one after the other

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

# First Triangle
row = 1
while row <= n:
    print((str(row) + " ") * row)
    row = row + 1

# Second Triangle
row = 1
while row <= n:
    print((str(row) + " ") * row)
    row = row + 1
```

---

## 🧪 **Sample Input:**

```
3
```

## 🧾 **Sample Output:**

```
1
2 2
3 3 3
1
2 2
3 3 3
```

---
