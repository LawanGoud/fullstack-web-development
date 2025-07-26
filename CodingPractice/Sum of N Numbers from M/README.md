## 🧩 **Problem Name:**

**Sum of N Numbers from M**

---

## 🎯 **Goal:**

✅ Read two numbers:

- `M` = starting number
- `N` = count of numbers
  ✅ Calculate the **sum** of N numbers starting from M
  ✅ Print the result

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- Counting
- Arithmetic operations
- Accumulating a total

---

## ✅ **Code:**

```python
# Read the starting number M
start = int(input())

# Read how many numbers to sum
count = int(input())

# Initialize a counter and sum variable
i = 0
total = 0

# Loop to add N numbers starting from M
while i < count:
    total = total + (start + i)
    i = i + 1

# Print the total sum
print(total)
```

---

## 🧪 **Sample Input:**

```
7
3
```

## 🧾 **Sample Output:**

```
24
```

---
