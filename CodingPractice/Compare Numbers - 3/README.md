## 🧩 **Problem Name:**

**Compare Numbers - 3**

---

## 🎯 **Goal:**

Write a program that:

✅ Reads two numbers `A` and `B`
✅ Checks if **either**:

- Both `A` and `B` are **positive numbers** (`> 0`)
  **OR**
- Both `A` and `B` are **less than 70**

✅ Prints `True` if **either condition** is true, otherwise `False`

---

## 🧠 **Concepts Used:**

- Logical operators: `and`, `or`
- Comparison operators: `<`, `>`
- Integer input and boolean logic

---

## 🪜 **Step-by-Step Explanation**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if both are positive

```python
both_positive = A > 0 and B > 0
```

---

### ✅ Step 3: Check if both are less than 70

```python
both_less_than_70 = A < 70 and B < 70
```

---

### ✅ Step 4: Check if either condition is true

```python
result = both_positive or both_less_than_70
```

---

### ✅ Step 5: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
200
50
```

### 🧾 Explanation:

- `A = 200`, `B = 50`
- Both are positive → ✅ `True`
- One of them is **not less than 70** → ❌
  ✅ At least one condition is satisfied → Output: `True`

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

both_positive = A > 0 and B > 0
both_less_than_70 = A < 70 and B < 70

result = both_positive or both_less_than_70
print(result)
```

---

Let me know if you'd like a version with labeled outputs like:

```
Result: True
```
