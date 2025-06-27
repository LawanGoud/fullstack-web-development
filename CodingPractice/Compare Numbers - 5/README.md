## 🧩 **Problem Name:**

**Compare Numbers - 5**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if:

- **One** of the numbers is **negative**, and
- The **product** of `A` and `B` is **greater than or equal to -46**
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators (`and`, `or`)
- Comparison operators
- Product calculation with `*`
- Conditional expressions

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check both conditions:

1. **One** of the numbers is negative:

   ```python
   (A < 0 or B < 0)
   ```

2. **Product is greater than or equal to -46**:

   ```python
   (A * B >= -46)
   ```

Combine both with `and`:

```python
result = (A < 0 or B < 0) and (A * B >= -46)
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
1
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

# Check if one is negative and product >= -46
result = (A < 0 or B < 0) and (A * B >= -46)

print(result)
```
