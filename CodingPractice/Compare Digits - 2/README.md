## 🧩 **Problem Name:**

**Compare Digits - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **two-digit number** `N` (as a string)
✅ Checks if:

- `N` is **greater than 25**, and
- The **first digit** is **greater than** the **second digit**
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- String indexing (`word[0]`)
- Type casting (`int()`)
- Logical operator `and`
- Integer comparison (`>`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number as a string

```python
N = input()
```

---

### ✅ Step 2: Extract digits and convert to integers

```python
first_digit = int(N[0])
second_digit = int(N[1])
```

---

### ✅ Step 3: Convert full number to integer for numeric comparison

```python
number = int(N)
```

---

### ✅ Step 4: Check the conditions

```python
result = (number > 25) and (first_digit > second_digit)
```

---

### ✅ Step 5: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
24
```

### 🧾 Sample Output:

```
False
```

---

## ✅ Full Code:

```python
N = input()

first_digit = int(N[0])
second_digit = int(N[1])
number = int(N)

# Check if number > 25 and first digit > second digit
result = (number > 25) and (first_digit > second_digit)

print(result)
```

---
