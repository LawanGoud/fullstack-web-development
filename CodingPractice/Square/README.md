## 🧩 **Problem Name:**

**Square**

---

## ❓ **Goal:**

Write a program that:

✅ Reads a number `N`
✅ Prints a **square** of `N` rows and `N` columns
✅ Each cell contains a `*` followed by a space
✅ The same line is printed `N` times

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
# Read the number of rows and columns
n = int(input())

# Create a line with N stars followed by space
line = ("* " * n)

# Counter to control rows
row = 1

# Print the line N times
while row <= n:
    print(line)
    row = row + 1
```

---

## 🧪 **Sample Input:**

```
3
```

## 🧾 **Sample Output:**

```
* * *
* * *
* * *
```

---
