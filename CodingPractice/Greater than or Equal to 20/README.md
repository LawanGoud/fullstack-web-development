## 🧩 **Problem Name:**

**Greater than or Equal to 20**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads **three integers**: `A`, `B`, and `C`
✅ Checks if **each number** is **greater than or equal to 20**
✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Relational operator: `>=`
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

### ✅ Step 2: Check the condition

```python
result = (A >= 20) and (B >= 20) and (C >= 20)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
10
20
30
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
C = int(input())

# Check if all numbers are greater than or equal to 20
result = (A >= 20) and (B >= 20) and (C >= 20)

print(result)
```

---
