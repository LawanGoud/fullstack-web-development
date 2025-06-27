## 🧩 **Problem Name:**

**Not Negative**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers: `A` and `B`
✅ Checks if **both numbers are not negative** (i.e., both are **greater than or equal to 0**)
✅ Prints `True` if the condition is satisfied, else `False`

---

## 🧠 **Concepts Used:**

- Comparison operator (`>=`)
- Logical operator (`and`)
- `input()` to read values
- `int()` for type conversion

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if both are not negative

```python
result = A >= 0 and B >= 0
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
10
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

result = A >= 0 and B >= 0
print(result)
```
