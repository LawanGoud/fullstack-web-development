## 🧩 **Problem Name:**

**Between 40 and 140**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers `A` and `B`
✅ Checks if:

* **Any** of the numbers is **between 40 and 140** (inclusive)

🔹 If **yes**, print:

```
Between 40 and 140: Yes
```

🔹 Otherwise, print:

```
Between 40 and 140: No
```

---

## 🧠 **Concepts Used:**

* Logical operator: `or`
* Comparison operators: `>=`, `<=`
* Conditional statements: `if-else`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read two numbers

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Apply condition using logical `or`

```python
(40 <= A <= 140) or (40 <= B <= 140)
```

---

### ✅ Step 3: Use `if-else` to print result

---

## 🧪 Sample Input:

```
12
100
```

### 🧾 Sample Output:

```
Between 40 and 140: Yes
```

---

## ✅ Full Code:

```python
# Read the first number
A = int(input())

# Read the second number
B = int(input())

# Check if A or B is between 40 and 140 (inclusive)
if (40 <= A <= 140) or (40 <= B <= 140):
    # If yes, print the appropriate message
    print("Between 40 and 140: Yes")
else:
    # Otherwise, print no
    print("Between 40 and 140: No")
```

---

