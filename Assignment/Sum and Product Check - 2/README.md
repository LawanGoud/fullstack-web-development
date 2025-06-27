## 🧩 **Problem Name:**

**Sum and Product Check - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if:

- The **sum** of `A` and `B` is **negative**, **or**
- The **product** of `A` and `B` is **negative**
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Arithmetic operations (`+`, `*`)
- Comparison operators (`<`)
- Logical operators (`or`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if sum or product is negative

```python
result = (A + B < 0) or (A * B < 0)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
5
-3
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

result = (A + B < 0) or (A * B < 0)

print(result)
```

---
