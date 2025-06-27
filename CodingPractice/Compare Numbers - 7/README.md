## 🧩 **Problem Name:**

**Compare Numbers - 7**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **four-digit number** as a string
✅ Checks if:

- The **first two digits** are equal to `19`, and
- The **last two digits** are **between 30 and 60 (inclusive)**

✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- String slicing (`[:2]`, `[2:]`)
- Type conversion: `int()`
- Logical operators (`and`)
- Comparison operators

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number as a string

```python
N = input()
```

---

### ✅ Step 2: Extract parts using slicing

```python
first_two = N[:2]       # First two characters
last_two = int(N[2:])   # Convert last two characters to integer
```

---

### ✅ Step 3: Check the condition

```python
result = (first_two == "19") and (30 <= last_two <= 60)
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
1947
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
N = input()

first_two = N[:2]
last_two = int(N[2:])

result = (first_two == "19") and (30 <= last_two <= 60)

print(result)
```

---
