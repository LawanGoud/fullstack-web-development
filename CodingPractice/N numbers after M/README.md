## 🧩 **Problem Name:**

**N Numbers After M**

---

## 🎯 **Goal:**

✅ Read two integers `M` and `N`
✅ Print **N numbers after M**, each on a new line

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- Counting and incrementing
- Basic arithmetic

---

## ✅ **Code:**

```python
# Read the starting number M
start = int(input())

# Read how many numbers to print after M
total = int(input())

# Initialize a counter
count = 1

# Loop to print N numbers after M
while count <= total:
    print(start + count)
    count = count + 1
```

---

## 🧪 **Sample Input:**

```
3
5
```

## 🧾 **Sample Output:**

```
4
5
6
7
8
```

---
