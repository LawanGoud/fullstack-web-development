
## 🧩 **Problem Name:**

**Valid Triangle - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three integers `A`, `B`, and `C` (angles of a triangle)
✅ Checks if the **sum** of the angles is exactly `180`
✅ If yes, print:

```
*  
**  
***  
```

✅ Else, print:

```
Not a Valid Triangle
```

---

## 🧠 **Concepts Used:**

* Input reading using `input()`
* Type conversion using `int()`
* Conditional statements (`if`, `else`)
* Angle sum property of a triangle

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read three angles as input

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check if their sum is 180

```python
if A + B + C == 180:
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")
```

---

## 🧪 Sample Input:

```
60  
45  
75
```

### 🧾 Sample Output:

```
*  
**  
***
```

---

## ✅ Full Code:

```python
# Read three angles of the triangle
A = int(input())
B = int(input())
C = int(input())

# Check if the sum of angles is equal to 180
if A + B + C == 180:
    # Print the triangle pattern
    print("*")
    print("**")
    print("***")
else:
    # If not equal to 180, it's not a valid triangle
    print("Not a Valid Triangle")
```

---

