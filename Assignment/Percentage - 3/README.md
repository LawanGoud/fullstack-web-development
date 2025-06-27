## 🧩 **Problem Name:**

**Percentage – 3**

---

## 📝 **Task:**

Write a program that:

- Takes two integer inputs:

  - `P` – percentage
  - `N` – a number

- Checks if **P percent of 500** is equal to `N`.

---

## 💡 **Concepts Used:**

- Integer input using `int(input())`
- Percentage formula
- Comparison operator `==`

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read two integer inputs

```python
P = int(input())
N = int(input())
```

---

### ✅ Step 2: Calculate `P%` of 500

```python
value = (P * 500) // 100
```

🔸 Since we're working with integers, we use `//` (integer division) to ensure `value` remains an integer.

---

### ✅ Step 3: Compare calculated value with `N`

```python
result = value == N
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs
P = int(input())
N = int(input())

# Step 2: Calculate P% of 500
value = (P * 500) // 100

# Step 3: Compare with given number
result = value == N

# Step 4: Print result
print(result)
```

---

## 🧪 Sample Input:

```
50
250
```

## 🎯 Sample Output:

```
True
```
