## 🧩 **Problem Name:**

**Positive Integer**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer `N`
✅ If the number is **negative**, convert it to a **positive number**
✅ Otherwise, print the number as is
✅ Prints the result

---

## 🧠 **Concepts Used:**

- Conditional statements (`if-else`)
- Integer comparison (`<`)
- `print()` function

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number

```python
N = int(input())
```

---

### ✅ Step 2: Check if the number is negative

```python
if N < 0:
    N = -N   # Convert to positive
```

---

### ✅ Step 3: Print the result

```python
print(N)
```

---

## 🧪 Sample Input:

```
-5
```

### 🧾 Sample Output:

```
5
```

---

## ✅ Full Code:

```python
N = int(input())

if N < 0:
    N = -N

print(N)
```
