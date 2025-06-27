## 🧩 **Problem Name:**

**Compare with Ten**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if **any** of the following conditions is satisfied:

- The **sum** of `A` and `B` is **less than 10**
- The **difference** between `A` and `B` is **less than 10**
- `A` is **between 5 and 30** (inclusive)

✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Arithmetic operations: addition, subtraction
- Logical operator: `or`
- Relational comparisons
- Absolute value with `abs()`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Evaluate the three conditions

1. Sum less than 10:

   ```python
   A + B < 10
   ```

2. Absolute difference less than 10:

   ```python
   abs(A - B) < 10
   ```

3. A between 5 and 30 (inclusive):

   ```python
   5 <= A <= 30
   ```

Combine all with `or`:

```python
result = (A + B < 10) or (abs(A - B) < 10) or (5 <= A <= 30)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
12
8
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

# Check conditions
result = (A + B < 10) or (abs(A - B) < 10) or (5 <= A <= 30)

print(result)
```

---
