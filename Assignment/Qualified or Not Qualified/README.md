## 🧩 **Problem Name:**

**Qualified or Not Qualified**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads the marks `M` in Maths and `P` in Physics
✅ Checks if:

* **Both M and P > 35**, **OR**
* **Sum of M and P ≥ 100**

✅ If any condition is satisfied, print `"Qualified"`
✅ Otherwise, print `"Not Qualified"`

---

## 🧠 **Concepts Used:**

* Comparison operators (`>`, `>=`)
* Logical operators (`and`, `or`)
* Input and output
* Conditional statements

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the marks

```python
M = int(input())  
P = int(input())
```

---

### ✅ Step 2: Check qualification conditions

```python
if (M > 35 and P > 35) or (M + P >= 100):  
    print("Qualified")  
else:  
    print("Not Qualified")
```

---

## 🧪 Sample Input:

```
50  
40
```

### 🧾 Sample Output:

```
Qualified
```

---

## ✅ Full Code:

```python
# Read marks in Maths
M = int(input())

# Read marks in Physics
P = int(input())

# Check if both marks are greater than 35 or if their total is 100 or more
if (M > 35 and P > 35) or (M + P >= 100):
    # If either condition is satisfied, print Qualified
    print("Qualified")
else:
    # If none of the conditions are satisfied, print Not Qualified
    print("Not Qualified")
```

---

