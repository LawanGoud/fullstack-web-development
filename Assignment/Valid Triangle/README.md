## 🧩 **Problem Name:**

**Valid Triangle**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `A`, `B`, and `C` representing the sides of a triangle
✅ Checks if the **sum of any two sides** is **always greater than the third side**
✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Triangle inequality rule
- Logical operators (`and`)
- Comparison operators (`>`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Apply the triangle inequality rule

For a triangle to be valid:

- A + B > C
- A + C > B
- B + C > A

```python
result = (A + B > C) and (A + C > B) and (B + C > A)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
3
4
5
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

result = (A + B > C) and (A + C > B) and (B + C > A)

print(result)
```

---
