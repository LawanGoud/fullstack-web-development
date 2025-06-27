## 🧩 **Problem Name:**

**Greater than Five**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if:

- **Both** numbers are **positive**
- **At least one** of them is **greater than 5**
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators (`and`, `or`)
- Comparison operators (`>`)
- Boolean logic with compound conditions

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check both conditions

1. **Both are positive**:

   ```python
   A > 0 and B > 0
   ```

2. **At least one is greater than 5**:

   ```python
   A > 5 or B > 5
   ```

Combine both with `and`:

```python
result = (A > 0 and B > 0) and (A > 5 or B > 5)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
-10
6
```

### 🧾 Sample Output:

```
False
```

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

# Check if both numbers are positive and at least one is greater than 5
result = (A > 0 and B > 0) and (A > 5 or B > 5)

print(result)
```

---
