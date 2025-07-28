## 🧩 **Problem Name:**

**Square - 2 (No Nested Loops)**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Print a square of `N x N` where each line contains the same number (equal to the row number)
✅ Avoid using nested loops

---

## ✅ **Code with Explanation:**

```python
# Read the number N
n = int(input())

# Initialize the row counter
count = 1

# Repeat for each row
while count <= n:
    # Form a line by repeating the row number N times
    print(str(count) * n)
    count = count + 1
```

---

## 💡 How It Works:

- `str(count) * n` will repeat the row number as a string `n` times (e.g., `"2"*3 → "222"`)
- This avoids the need for an inner loop

---

## 🧪 Sample Input:

```
3
```

## 🧾 Sample Output:

```
111
222
333
```

---
