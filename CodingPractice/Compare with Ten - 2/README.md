## 🧩 **Problem Name:**

**Compare with Ten - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads **three integers** `A`, `B`, and `C`
✅ Checks if the **sum of any two numbers** is **always greater than 10**
✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- `input()` and `int()`
- arithmetic operators (`+`)
- comparison operator (`>`)
- logical operator (`and`)
- `print(...)`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the inputs

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check all three pairwise sums

We need all of these to be greater than 10:

- A + B > 10
- A + C > 10
- B + C > 10

```python
result = (A + B > 10) and (A + C > 10) and (B + C > 10)
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
4
8
17
```

## 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())
C = int(input())

result = (A + B > 10) and (A + C > 10) and (B + C > 10)

print(result)
```

---
