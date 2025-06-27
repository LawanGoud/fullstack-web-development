## 🧩 **Problem Name:**

**Same Digits**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **three-digit number** (as input)
✅ Checks if **all the digits** are the **same**
✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Reading input as a string
- String slicing/indexing
- Comparison of characters (digits)
- Boolean logic

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number as a string

```python
num = input()
```

---

### ✅ Step 2: Compare the digits using slicing

```python
result = (num[0] == num[1]) and (num[1] == num[2])
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
222
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
num = input()

result = (num[0] == num[1]) and (num[1] == num[2])

print(result)
```

---
