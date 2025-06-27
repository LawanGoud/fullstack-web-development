## 🧩 **Problem Name:**

**Lucky Number**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers `A` and `B`
✅ Checks if **any** of the following conditions is satisfied:

* `A` is equal to 6 **or** `B` is equal to 6
* The **sum** of `A` and `B` is equal to 6
* The **difference** between `A` and `B` (i.e., `A - B` or `B - A`) is equal to 6

🔹 If any condition is satisfied, print **Lucky**
🔹 Otherwise, print **Not Lucky**

---

## 🧠 **Concepts Used:**

* Comparison operators: `==`
* Arithmetic operations: `+`, `-`
* Logical operator: `or`
* Conditional statements: `if-else`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check for the conditions mentioned

---

## 🧪 Sample Input:

```
4
10
```

### 🧾 Sample Output:

```
Lucky
```

---

## ✅ Full Code:

```python
# Read first number
A = int(input())

# Read second number
B = int(input())

# Check if A or B is 6 OR sum is 6 OR difference is 6
if A == 6 or B == 6 or A + B == 6 or A - B == 6 or B - A == 6:
    # If any condition is true, print Lucky
    print("Lucky")
else:
    # Otherwise, print Not Lucky
    print("Not Lucky")
```

---

