## 🧩 **Problem Name:**

**Sum of N Squares**

---

## ❓ **Goal:**

✅ Read a number `N`
✅ Print the **sum of squares** of numbers from **1 to N**

🧮 Example:
For N = 4 → $1^2 + 2^2 + 3^2 + 4^2 = 30$

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- multiplication `*`
- addition `+`
- `print()`

---

## ✅ **Code with Explanation:**

```python
# Read the number N
n = int(input())

# Start from 1
num = 1

# Initialize the sum to 0
sum_of_squares = 0

# Loop from 1 to N
while num <= n:
    square = num * num           # Calculate square of the current number
    sum_of_squares = sum_of_squares + square  # Add square to sum
    num = num + 1                # Move to the next number

# Print the final result
print(sum_of_squares)
```

---

## 🧪 **Sample Input:**

```
4
```

## 🧾 **Sample Output:**

```
30
```

---
