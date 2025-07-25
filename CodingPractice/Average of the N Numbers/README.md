## 🧩 **Problem Name:**

**Average of the N Numbers**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Calculate the average of numbers from 1 to N
✅ Print the average

---

## 🧠 **Concepts Used:**

- Input and output
- While loop
- Arithmetic operations
- Variables

---

## 🧮 **Formula Used:**

Average of N numbers from 1:

```
Average = (1 + 2 + 3 + ... + N) / N
        = Sum of N numbers / N
```

---

## ✅ **Code:**

```python
# Read the number N
limit = int(input())

# Initialize the starting number and sum
number = 1
total = 0

# Loop to calculate the sum from 1 to N
while number <= limit:
    total = total + number
    number = number + 1

# Calculate the average
average = total / limit

# Print the result
print(average)
```

---

## 🧪 **Sample Input:**

```
4
```

## 🧾 **Sample Output:**

```
2.5
```

---
