## 🧩 **Problem Name:**

**Compare Numbers - 9**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **three-digit number** as a string
✅ Checks if **any** of the following is `True`:

- All three digits are **greater than 7**, **OR**
- The product of **any two digits** is **less than or equal to 30**
  ✅ Then print `True` or `False`

---

## 🧠 **Concepts Used:**

- String indexing
- Type conversion to `int`
- Arithmetic operations
- Logical operators: `and`, `or`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number

```python
N = input()
```

---

### ✅ Step 2: Convert each character to an integer

```python
a = int(N[0])
b = int(N[1])
c = int(N[2])
```

---

### ✅ Step 3: Check both conditions

```python
# Condition 1: All digits are greater than 7
all_gt_7 = (a > 7) and (b > 7) and (c > 7)

# Condition 2: Product of any two digits is <= 30
product_check = (a * b <= 30) and (b * c <= 30) and (a * c <= 30)

# Final result: Either condition is True
result = all_gt_7 or product_check
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
832
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
N = input()

a = int(N[0])
b = int(N[1])
c = int(N[2])

all_gt_7 = (a > 7) and (b > 7) and (c > 7)
product_check = (a * b <= 30) and (b * c <= 30) and (a * c <= 30)

result = all_gt_7 or product_check

print(result)
```

---
