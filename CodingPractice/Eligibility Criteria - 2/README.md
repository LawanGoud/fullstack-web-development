## 🧩 **Problem Name:**

**Eligibility Criteria - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers: `M` (Maths), `P` (Physics), and `C` (Chemistry)
✅ Checks if **both** of the following conditions are satisfied:

- `M + P >= 100` **OR** `P + C >= 100` **OR** `M + C >= 100`
- Total marks `M + P + C >= 180`

✅ Then print `True` or `False`

---

## 🧠 **Concepts Used:**

- Integer input
- Arithmetic operations
- Logical operators: `and`, `or`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input marks

```python
M = int(input())
P = int(input())
C = int(input())
```

---

### ✅ Step 2: Check the two conditions

```python
condition1 = (M + P >= 100) or (P + C >= 100) or (M + C >= 100)
condition2 = (M + P + C >= 180)
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
82
55
45
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

condition1 = (M + P >= 100) or (P + C >= 100) or (M + C >= 100)
condition2 = (M + P + C >= 180)

result = condition1 and condition2

print(result)
```

---
