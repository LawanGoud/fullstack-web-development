### 🧩 **Problem Name:**

**Digit Zero**

---

### 🎯 **Goal:**

Write a program that:
✅ Reads a three-digit number as a string
✅ Checks if it contains the digit `'0'`
✅ Prints `True` if it does, otherwise `False`

---

### 🧠 **Concepts Used:**

- `input()`
- string indexing
- equality operator (`==`)
- logical operator (`or`)
- `print(...)`

---

### 🪜 **Step-by-Step Solution**

#### ✅ Step 1: Read the number as a string

```python
num = input()
```

#### ✅ Step 2: Check if any digit is `'0'`

```python
result = (num[0] == '0') or (num[1] == '0') or (num[2] == '0')
```

#### ✅ Step 3: Print the result

```python
print(result)
```

---

### 🧪 Sample Input:

```
120
```

### 🧾 Sample Output:

```
True
```

---

### ✅ Full Code:

```python
num = input()

result = (num[0] == '0') or (num[1] == '0') or (num[2] == '0')

print(result)
```

---
