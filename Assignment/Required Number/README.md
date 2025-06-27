## 🧩 **Problem Name:**

**Required Number**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer `N`
✅ Checks if:

- `N` is between **50 and 100**, **or**
- The **first digit** of `N` is **equal to 7**
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Logical operators (`or`)
- Comparison operators (`<=`, `>=`, `==`)
- String slicing to get the first digit

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number

```python
N = int(input())
```

---

### ✅ Step 2: Convert to string and get first digit

```python
first_digit = str(N)[0]
```

---

### ✅ Step 3: Check the conditions

```python
result = (N >= 50 and N <= 100) or (first_digit == '7')
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
54
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
N = int(input())

first_digit = str(N)[0]

result = (N >= 50 and N <= 100) or (first_digit == '7')

print(result)
```

---
