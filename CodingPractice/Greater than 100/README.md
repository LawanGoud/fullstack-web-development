## 🧩 **Problem Name:**

**Greater than 100**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `A`, `B`, and `C`
✅ Checks if **each number** is **greater than 100**
✅ If **all three** numbers are greater than 100, print:

```
All are greater than 100
```

✅ Otherwise, print:

```
Not all the greater than 100
```

---

## 🧠 **Concepts Used:**

* Input reading using `input()`
* Type conversion using `int()`
* Logical operator `and`
* Conditional statements (`if`, `else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read three numbers as input

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check the condition

```python
if A > 100 and B > 100 and C > 100:
    print("All are greater than 100")
else:
    print("Not all the greater than 100")
```

---

## 🧪 Sample Input:

```
110  
256  
6350
```

### 🧾 Sample Output:

```
All are greater than 100
```

---

## ✅ Full Code:

```python
# Read three numbers from input
A = int(input())
B = int(input())
C = int(input())

# Check if all three numbers are greater than 100
if A > 100 and B > 100 and C > 100:
    # If all are greater than 100, print the message
    print("All are greater than 100")
else:
    # If any number is not greater than 100, print this message
    print("Not all the greater than 100")
```

---

