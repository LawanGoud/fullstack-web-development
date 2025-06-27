## 🧩 **Problem Name:**

**Eligibility Criteria - 4**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `M`, `P`, and `C` (marks in Maths, Physics, and Chemistry)
✅ Checks if **any** of the following conditions is satisfied:

- ✅ `M >= 60` and `P >= 50` and `C >= 45` and the **total** `M + P + C >= 180`
  **OR**
- ✅ `M + P >= 120` or `C + P >= 110`

✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators (`and`, `or`)
- Comparison operators (`>=`)
- Addition for total and subject combinations

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input values

```python
M = int(input())
P = int(input())
C = int(input())
```

---

### ✅ Step 2: Check both eligibility conditions

#### Condition 1:

```python
cond1 = M >= 60 and P >= 50 and C >= 45 and (M + P + C >= 180)
```

#### Condition 2:

```python
cond2 = (M + P >= 120) or (C + P >= 110)
```

---

### ✅ Step 3: Final result (any one condition is enough)

```python
result = cond1 or cond2
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
60
50
70
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

cond1 = M >= 60 and P >= 50 and C >= 45 and (M + P + C >= 180)
cond2 = (M + P >= 120) or (C + P >= 110)

result = cond1 or cond2

print(result)
```

---
