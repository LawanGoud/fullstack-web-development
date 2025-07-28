## 🧩 **Problem Name:**

**Right Angled Triangle - 4**

---

## ❓ **Goal:**

✅ Read a number `N`
✅ Print two **Right Angled Triangles** of `N` rows
✅ Use stars `*`, with a **space after every star**

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `string multiplication`
- `print()`

---

## ✅ **Code with Explanation:**

```python
# Read the number of rows
n = int(input())

# First triangle
row = 1
while row <= n:
    print(("* ")*row)   # Print 'row' number of "* "
    row = row + 1

# Second triangle
row = 1
while row <= n:
    print(("* ")*row)
    row = row + 1
```

---

## 🧪 **Sample Input:**

```
3
```

## 🧾 **Sample Output:**

```
*
* *
* * *
*
* *
* * *
```

---
