## 🧩 **Problem Name:**

**Valid Triangle - 3**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `A`, `B`, and `C` representing the sides of a triangle
✅ Checks if the **sum of any two sides** is **greater than** the **third side**

🔹 If **all three conditions** are satisfied, print:

```
It's a Triangle
```

🔹 Otherwise, print:

```
It's not a Triangle
```

---

## 🧠 **Concepts Used:**

* Triangle inequality property
* Logical operators (`and`)
* Conditional statement (`if-else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Apply triangle inequality conditions

```python
A + B > C  
B + C > A  
C + A > B
```

All must be **true**.

---

### ✅ Step 3: Use `if-else` to print result

---

## 🧪 Sample Input:

```
4  
5  
3
```

### 🧾 Sample Output:

```
It's a Triangle
```

---

## ✅ Full Code:

```python
# Read three sides of a triangle
A = int(input())
B = int(input())
C = int(input())

# Check if the sum of any two sides is greater than the third
if A + B > C and B + C > A and C + A > B:
    # If all conditions are satisfied, it's a triangle
    print("It's a Triangle")
else:
    # Otherwise, it's not a triangle
    print("It's not a Triangle")
```

---

