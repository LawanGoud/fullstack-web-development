ss## 🧩 **Problem Name:**

**Product of N Inputs**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Read `N` numbers (one by one)
✅ Multiply all numbers
✅ Print the final product

---

## 🧠 **Concepts Used:**

- Input/output
- `while` loop
- Multiplication
- Counter and accumulator

---

## ✅ **Code with Explanation:**

```python
# Read how many numbers to multiply
n = int(input())

# Start with product as 1 (multiplicative identity)
product = 1

# Start counter from 1
count = 1

# Loop N times
while count <= n:
    number = int(input())     # Read a number
    product = product * number  # Multiply it to current product
    count = count + 1         # Increase the counter

# Print the final product
print(product)
```

---

## 🧪 **Sample Input:**

```
3
2
3
7
```

## 🧾 **Sample Output:**

```
42
```

---
