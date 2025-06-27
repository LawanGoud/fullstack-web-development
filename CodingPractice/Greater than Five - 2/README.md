## 🧩 **Problem Name:**

**Greater than Five - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads **three integers**: `A`, `B`, and `C`
✅ Checks if **each** of the numbers is **greater than 5**
✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Relational operator: `>`
- Logical operator: `and`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check if all three numbers are greater than 5

```python
result = (A > 5) and (B > 5) and (C > 5)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
7
18
239
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
C = int(input())

# Check if all numbers are greater than 5
result = (A > 5) and (B > 5) and (C > 5)

print(result)
```

---
