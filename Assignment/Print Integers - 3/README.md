## 🧩 **Problem Name:**

**Print Integers - 3**

---

## ❓ **Goal:**

✅ Read a number `N`
✅ Print the integers from `N` down to `1`, one number per line

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `print()`
- decrementing a number using `- 1`

---

## ✅ **Code with Explanation:**

```python
# Read the number N
n = int(input())

# Start from N
current = n

# Repeat until current becomes 0
while current >= 1:
    print(current)     # Print the current number
    current = current - 1  # Decrease the number by 1
```

---

## 🧪 **Sample Input:**

```
5
```

## 🧾 **Sample Output:**

```
5
4
3
2
1
```

---
