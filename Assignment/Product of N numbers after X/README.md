## 🧩 **Problem Name:**

**Product of N Numbers After X**

---

## ❓ **Goal:**

✅ Read two numbers `X` and `N`
✅ Print the **product** of `N` numbers starting **after X**
→ That is: Multiply numbers from `(X + 1)` to `(X + N)`

---

## 🧠 **Concepts Used:**

- `input()`
- `int()`
- `while` loop
- multiplication `*`
- simple variable usage
- `print()`

---

## ✅ **Code with Explanation:**

```python
# Read the starting number X
x = int(input())

# Read how many numbers to multiply
n = int(input())

# Initialize starting value (X + 1)
num = x + 1

# Initialize product as 1 (identity for multiplication)
product = 1

# Count of numbers multiplied so far
count = 0

# Loop to multiply N numbers
while count < n:
    product = product * num
    num = num + 1
    count = count + 1

# Print the final product
print(product)
```

---

## 🧪 **Sample Input:**

```
4
2
```

## 🧾 **Sample Output:**

```
30
```

> ✅ Because numbers after 4 are `5` and `6`, and `5 * 6 = 30`

---
