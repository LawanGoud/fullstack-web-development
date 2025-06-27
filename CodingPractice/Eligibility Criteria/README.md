## 🧩 **Problem Name:**

**Eligibility Criteria**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads marks in **Maths (M)**, **Physics (P)**, and **Chemistry (C)**
✅ Checks if **any** of the following conditions is satisfied:

- `M >= 70` and `P >= 60` and `C >= 60`
- Sum of all marks `M + P + C >= 180`
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators: `and`, `or`
- Relational comparisons
- Summation of values

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
M = int(input())
P = int(input())
C = int(input())
```

---

### ✅ Step 2: Check both eligibility conditions

1. All subject minimums:

   ```python
   M >= 70 and P >= 60 and C >= 60
   ```

2. Total marks:

   ```python
   M + P + C >= 180
   ```

Use `or` to combine the conditions:

```python
result = (M >= 70 and P >= 60 and C >= 60) or (M + P + C >= 180)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
0
100
100
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
M = int(input())
P = int(input())
C = int(input())

# Check eligibility conditions
result = (M >= 70 and P >= 60 and C >= 60) or (M + P + C >= 180)

print(result)
```

---
