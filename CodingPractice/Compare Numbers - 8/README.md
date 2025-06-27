## 🧩 **Problem Name:**

**Compare Numbers - 8**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **three-digit number** as a string
✅ Checks if all the following are `True`:

- The number contains the digit `1` (check using slicing/indexing only)
- The sum of digits is less than 12
- The last digit is `5`
  ✅ Then print `True` or `False`

---

## 🧠 **Concepts Used:**

- String indexing (e.g., `N[0]`)
- Type conversion using `int()`
- Logical operators: `and`
- Comparison operators

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input

```python
N = input()
```

---

### ✅ Step 2: Convert characters to digits

```python
a = int(N[0])
b = int(N[1])
c = int(N[2])
```

---

### ✅ Step 3: Check conditions using only learned logic

```python
# Check if any digit is 1
is_one = (N[0] == '1') or (N[1] == '1') or (N[2] == '1')

# Check if sum of digits is less than 12
sum_less = (a + b + c) < 12

# Check if last digit is 5
last_is_five = N[2] == '5'

# Final result
result = is_one and sum_less and last_is_five
```

---

### ✅ Step 4: Print result

```python
print(result)
```

---

## 🧪 Sample Input:

```
315
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
N = input()

a = int(N[0])
b = int(N[1])
c = int(N[2])

is_one = (N[0] == '1') or (N[1] == '1') or (N[2] == '1')
sum_less = (a + b + c) < 12
last_is_five = N[2] == '5'

result = is_one and sum_less and last_is_five

print(result)
```

---
