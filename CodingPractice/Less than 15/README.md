## 🧩 **Problem Name:**

**Less than 15**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads **three numbers**: `A`, `B`, and `C`
✅ Checks if **any one** of them is **less than 15**
✅ Prints `True` if **at least one** is `< 15`, else `False`

---

## 🧠 **Concepts Used:**

- Comparison operators (`<`)
- Logical operator (`or`)
- `input()` for reading values
- Type conversion (`int()`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read inputs as integers

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check if any value is less than 15

```python
result = A < 15 or B < 15 or C < 15
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
18
2
20
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

result = A < 15 or B < 15 or C < 15
print(result)
```

---
