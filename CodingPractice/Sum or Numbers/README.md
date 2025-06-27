## 🧩 **Problem Name:**

**Sum or Numbers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers `A` and `B`
✅ Checks if:

* One of `A` or `B` is **less than 20**
  **OR**
* The **sum** of `A` and `B` is **between 30 and 50** (inclusive)

🔹 If **any** condition is satisfied, print the **sum of A and B**
🔹 Otherwise, print `A` and `B` on separate lines

---

## 🧠 **Concepts Used:**

* Comparison operators: `<`, `<=`, `>=`
* Logical operator: `or`
* Conditional statements: `if-else`
* Arithmetic operation: `+`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check if A < 20 or B < 20 or (A + B is between 30 and 50)

```python
if A < 20 or B < 20 or (30 <= A + B <= 50):
```

---

### ✅ Step 3: Print sum or individual values based on condition

---

## 🧪 Sample Input:

```
45
7
```

### 🧾 Sample Output:

```
52
```

---

## ✅ Full Code:

```python
# Read first number
A = int(input())

# Read second number
B = int(input())

# Check if one number is less than 20 OR sum is between 30 and 50
if A < 20 or B < 20 or (30 <= A + B <= 50):
    # If condition is satisfied, print the sum
    print(A + B)
else:
    # Otherwise, print A and B on separate lines
    print(A)
    print(B)
```

---
