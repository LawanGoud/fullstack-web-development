## 🧩 **Problem Name:**

**Compare Numbers - 2**

---

## 🎯 **Goal:**

Write a program that:

✅ Takes **two integer inputs** A and B
✅ Checks **two conditions**:

1. One of the numbers is **negative**
2. The **sum** of the two numbers is **greater than 7**

✅ Prints `True` if **both conditions** are satisfied, else prints `False`

---

## 🧠 **Concepts Used:**

- Logical operators: `and`, `or`
- Comparison operators: `<`, `>`
- Integer input and arithmetic

---

## 🪜 **Step-by-Step Explanation**

### ✅ Step 1: Read two integer inputs

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if one of the numbers is negative

```python
one_negative = A < 0 or B < 0
```

---

### ✅ Step 3: Check if the sum is greater than 7

```python
sum_greater_than_7 = (A + B) > 7
```

---

### ✅ Step 4: Combine both conditions

```python
result = one_negative and sum_greater_than_7
```

---

### ✅ Step 5: Print the result

```python
print(result)
```

---

## 💡 Example

### 🧪 Sample Input:

```
13
-3
```

### 🧾 Explanation:

- One number is negative: ✅ `-3 < 0` → True
- Sum is `13 + (-3) = 10` → `10 > 7` → ✅ True
  ✅ Both conditions are True → Final Output: `True`

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

one_negative = A < 0 or B < 0
sum_greater_than_7 = (A + B) > 7

result = one_negative and sum_greater_than_7
print(result)
```

---
