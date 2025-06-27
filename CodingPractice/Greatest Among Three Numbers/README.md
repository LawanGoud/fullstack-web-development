## 🧩 **Problem Name:**

**Greatest Among Three Numbers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three numbers `A`, `B`, and `C`
✅ Prints the **greatest** among the three numbers

---

## 🧠 **Concepts Used:**

* Comparison operators: `>=`, `>`
* Conditional statements: `if`, `elif`, `else`
* `print()` function

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read three numbers

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Compare A, B, and C to find the greatest

---

## 🧪 Sample Input:

```
2
5
7
```

### 🧾 Sample Output:

```
7
```

---

## ✅ Full Code:

```python
# Read first number
A = int(input())

# Read second number
B = int(input())

# Read third number
C = int(input())

# Compare A, B, and C to find the greatest
if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)
```

---

