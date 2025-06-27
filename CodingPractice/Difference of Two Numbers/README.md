## 🧩 **Problem Name:**

**Difference of Two Numbers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers: `A`, `B`, and `C`
✅ Checks if the **difference between any two numbers** (`A - B`, `B - C`, `C - A`) is **always less than 25** (in **magnitude**)

🔹 If **all differences are less than 25**, print:

```
Difference is less than 25
```

🔹 Otherwise, print:

```
Difference is not less than 25
```

---

## 🧠 **Concepts Used:**

* Absolute difference using `abs()`
* Logical operator `and`
* Conditional statement (`if`, `else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read 3 input numbers

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check absolute difference of all required pairs

```python
abs(A - B) < 25  
abs(B - C) < 25  
abs(C - A) < 25
```

---

### ✅ Step 3: Use `if-else` to print result

---

## 🧪 Sample Input:

```
10  
5  
0
```

### 🧾 Sample Output:

```
Difference is less than 25
```

---

## ✅ Full Code:

```python
# Read the three numbers
A = int(input())
B = int(input())
C = int(input())

# Check if all differences are less than 25
if abs(A - B) < 25 and abs(B - C) < 25 and abs(C - A) < 25:
    # If all differences are within range, print this
    print("Difference is less than 25")
else:
    # Otherwise, print this
    print("Difference is not less than 25")
```

---
