## 🧩 **Problem Name:**

**Average of N Inputs**

---

## ❓ **Goal:**

✅ Read a number `N`
✅ Then read `N` integer inputs
✅ Print the average of those `N` numbers

📝 **Note:**
Average = (Sum of numbers) ÷ (Count of numbers)

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- `print()`
- Arithmetic operations (`+`, `/`)

---

## ✅ **Code with Explanation:**

```python
# Read how many numbers to input
n = int(input())

# Start with sum = 0 and count = 0
total = 0
count = 0

# Use while loop to read N numbers
while count < n:
    number = int(input())     # Read one number
    total = total + number    # Add it to total
    count = count + 1         # Move to next count

# Calculate average
average = total / n

# Print the average
print(average)
```

---

## 🧪 **Sample Input:**

```
5
3
6
2
8
1
```

## 🧾 **Sample Output:**

```
4.0
```

---
