## 🧩 **Problem Name:**

**Eligibility Criteria - 3**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `M`, `P`, and `C` (marks in Maths, Physics, and Chemistry)
✅ Checks if **both** the following conditions are satisfied:

- ✅ All three marks are **greater than or equal to 35**
- ✅ **Any two** subject marks **sum to 90 or more**

✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators (`and`, `or`)
- Comparison operators (`>=`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input values

```python
M = int(input())
P = int(input())
C = int(input())
```

---

### ✅ Step 2: Check both conditions

1. **Each mark is at least 35**

```python
condition1 = M >= 35 and P >= 35 and C >= 35
```

2. **Any two subjects sum to at least 90**

```python
condition2 = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)
```

---

### ✅ Step 3: Final result

```python
result = condition1 and condition2
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
50
35
40
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

condition1 = M >= 35 and P >= 35 and C >= 35
condition2 = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)

result = condition1 and condition2

print(result)
```

---
