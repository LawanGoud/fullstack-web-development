
## 🧩 **Problem Name:**

**Square or Rectangle**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers: **Length** and **Breadth**
✅ Checks:

* If both are equal → Print `"Square"`
* Otherwise → Print `"Rectangle"`

---

## 🧠 **Concepts Used:**

* Conditional statements (`if-else`)
* Equality operator (`==`)
* Input/output operations

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
length = int(input())
breadth = int(input())
```

---

### ✅ Step 2: Compare length and breadth

```python
if length == breadth:
    print("Square")
else:
    print("Rectangle")
```

---

## 🧪 Sample Input:

```
6
6
```

### 🧾 Sample Output:

```
Square
```

---

## ✅ Full Code:

```python
# Read the length of the box
length = int(input())

# Read the breadth of the box
breadth = int(input())

# Check if length and breadth are equal
if length == breadth:
    # If equal, it is a Square
    print("Square")
else:
    # If not equal, it is a Rectangle
    print("Rectangle")
```

---

