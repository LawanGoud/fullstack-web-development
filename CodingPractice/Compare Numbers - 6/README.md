## 🧩 **Problem Name:**

**Compare Numbers - 6**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **three-digit number** as a string
✅ Checks if:

- Each digit is **greater than 4**
  **OR**
- The **first digit** is **equal to 6**

✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- String indexing (`[]`)
- `input()` function
- Logical operators (`and`, `or`)
- Comparison of characters (converted to integers)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number as a string

```python
N = input()
```

---

### ✅ Step 2: Extract digits using slicing

```python
first = int(N[0])
middle = int(N[1])
last = int(N[2])
```

---

### ✅ Step 3: Check the condition

```python
result = (first > 4 and middle > 4 and last > 4) or (first == 6)
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
612
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
N = input()

first = int(N[0])
middle = int(N[1])
last = int(N[2])

result = (first > 4 and middle > 4 and last > 4) or (first == 6)

print(result)
```

---
