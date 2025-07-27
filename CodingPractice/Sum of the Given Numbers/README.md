## 🧩 **Problem Name:**

**Sum of the Given Numbers**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Read `N` integer inputs
✅ Find their **sum**
✅ Print the result

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- Addition
- Counter and accumulator

---

## ✅ **Code with Explanation:**

```python
# Read how many numbers we need to sum
total_numbers = int(input())

# Start the sum from 0 (additive identity)
sum_of_numbers = 0

# Set the counter to start from 1
count = 1

# Loop to read N numbers
while count <= total_numbers:
    current_number = int(input())      # Read each number
    sum_of_numbers = sum_of_numbers + current_number  # Add it to sum
    count = count + 1                  # Move to next number

# Print the final sum
print(sum_of_numbers)
```

---

## 🧪 **Sample Input:**

```
3
8
11
25
```

## 🧾 **Sample Output:**

```
44
```

---
