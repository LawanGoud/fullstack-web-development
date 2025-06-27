## 🧩 **Problem Name:**

**Discount**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two coupon codes `A` and `B`
✅ Checks if the **first three characters** of **either coupon** are `"DIS"`
✅ If so, print `"Discount"`
✅ Otherwise, print `"No Discount"`

---

## 🧠 **Concepts Used:**

* String slicing (`[:3]`)
* String comparison (`==`)
* Logical operator (`or`)
* Input and output

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input strings

```python
A = input()
B = input()
```

---

### ✅ Step 2: Check if first 3 characters of either code are "DIS"

```python
if A[:3] == "DIS" or B[:3] == "DIS":
    print("Discount")
else:
    print("No Discount")
```

---

## 🧪 Sample Input:

```
DISA9#5  
6BY@X
```

### 🧾 Sample Output:

```
Discount
```

---

## ✅ Full Code:

```python
# Read the first coupon code
A = input()

# Read the second coupon code
B = input()

# Check if the first three characters of either coupon code are "DIS"
if A[:3] == "DIS" or B[:3] == "DIS":
    # If condition is satisfied, print Discount
    print("Discount")
else:
    # Otherwise, print No Discount
    print("No Discount")
```

---

