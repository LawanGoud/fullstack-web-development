## 🧩 **Problem Name:**

**Sum of N Natural Numbers**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Find and print the **sum** of first `N` natural numbers
➡ Natural numbers start from **1**

---

## 🧠 **Concepts Used:**

- Input/output
- While loop
- Accumulator variable
- Natural numbers counting from 1

---

## ✅ **Code with Explanation:**

```python
# Read the value of N
n = int(input())

# Start counter from 1 (first natural number)
counter = 1

# Variable to store the sum
total = 0

# Loop to add numbers from 1 to N
while counter <= n:
    total = total + counter
    counter = counter + 1

# Print the final sum
print(total)
```

---

## 🧪 **Sample Input:**

```
6
```

## 🧾 **Sample Output:**

```
21
```

---
