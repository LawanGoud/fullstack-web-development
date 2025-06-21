## 🧩 **Problem Name:**

**Compare Numbers - 4**

---

## 🎯 **Goal:**

Write a program that:

✅ Reads two numbers `A` and `B`
✅ Checks if:

- **One** of the numbers is **less than 60**,
  **AND**
- **One** of the numbers is **greater than 80**

✅ Prints `True` if both conditions are satisfied, otherwise `False`.

---

## 🧠 **Concepts Used:**

- Logical operators: `and`, `or`
- Comparison operators: `<`, `>`
- Integer input

---

## 🪜 **Step-by-Step Explanation**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if one number is less than 60

```python
one_less_than_60 = A < 60 or B < 60
```

---

### ✅ Step 3: Check if one number is greater than 80

```python
one_greater_than_80 = A > 80 or B > 80
```

---

### ✅ Step 4: Final result using both conditions

```python
result = one_less_than_60 and one_greater_than_80
```

---

### ✅ Step 5: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
50
90
```

### 🧾 Explanation:

- 50 < 60 ✅
- 90 > 80 ✅
  Both conditions satisfied → ✅ `True`

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

one_less_than_60 = A < 60 or B < 60
one_greater_than_80 = A > 80 or B > 80

result = one_less_than_60 and one_greater_than_80
print(result)
```

---
