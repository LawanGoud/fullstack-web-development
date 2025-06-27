## 🧩 **Problem Name:**

**Sum and Product Check**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if:

- The **sum** of `A` and `B` has **less than three digits** (i.e., < 100), and
- The **product** of `A` and `B` has **less than three digits** (i.e., < 100)
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Arithmetic operations: `+` and `*`
- Integer comparison (`<`)
- Logical operator: `and`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Calculate sum and product

```python
sum_value = A + B
product_value = A * B
```

---

### ✅ Step 3: Check both conditions

```python
result = (sum_value < 100) and (product_value < 100)
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
17
4
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

sum_value = A + B
product_value = A * B

# Check if both sum and product have less than 3 digits
result = (sum_value < 100) and (product_value < 100)

print(result)
```

---
